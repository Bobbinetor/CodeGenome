#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>

#define BASE_URL "http://localhost:8888"
#define BUFFER_SIZE 2048

struct MemoryStruct {
    char *memory;
    size_t size;
};

/* Function to handle API response */
static size_t WriteMemoryCallback(void *contents, size_t size, size_t nmemb, void *userp) {
    size_t totalSize = size * nmemb;
    struct MemoryStruct *mem = (struct MemoryStruct *)userp;
    char *ptr = realloc(mem->memory, mem->size + totalSize + 1);
    if (ptr == NULL) return 0;
    mem->memory = ptr;
    memcpy(&(mem->memory[mem->size]), contents, totalSize);
    mem->size += totalSize;
    mem->memory[mem->size] = 0;
    return totalSize;
}

/* Function to make API calls */
int make_request(const char *method, const char *url, const char *data, char *response) {
    CURL *curl;
    CURLcode res;
    struct MemoryStruct chunk = {malloc(1), 0};
    
    curl_global_init(CURL_GLOBAL_ALL);
    curl = curl_easy_init();
    if (!curl) return -1;

    struct curl_slist *headers = NULL;
    headers = curl_slist_append(headers, "Content-Type: application/x-www-form-urlencoded");

    curl_easy_setopt(curl, CURLOPT_URL, url);
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteMemoryCallback);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *)&chunk);
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);

    if (strcmp(method, "POST") == 0 || strcmp(method, "PUT") == 0) {
        curl_easy_setopt(curl, CURLOPT_CUSTOMREQUEST, method);
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data);
    } else if (strcmp(method, "DELETE") == 0) {
        curl_easy_setopt(curl, CURLOPT_CUSTOMREQUEST, "DELETE");
    }

    res = curl_easy_perform(curl);
    if (res != CURLE_OK) {
        fprintf(stderr, "cURL request failed: %s\n", curl_easy_strerror(res));
    } else {
        strncpy(response, chunk.memory, BUFFER_SIZE - 1);
        response[BUFFER_SIZE - 1] = '\0';
    }

    free(chunk.memory);
    curl_easy_cleanup(curl);
    curl_global_cleanup();
    return res == CURLE_OK ? 0 : -1;
}

/* Function to run tests */
void run_tests() {
    char response[BUFFER_SIZE];

    printf("---- Running API Tests ----\n");

    // Test 1: List Items (Expect Empty)
    printf("\n[Test] GET /items (Expect Empty)\n");
    make_request("GET", BASE_URL "/items", NULL, response);
    printf("Response:\n%s\n", response);

    // Test 2: Create Item
    printf("\n[Test] POST /items (id=1, data=SampleData)\n");
    make_request("POST", BASE_URL "/items", "id=1&data=SampleData", response);
    printf("Response:\n%s\n", response);

    // Test 3: Retrieve Item
    printf("\n[Test] GET /items/1 (Expect SampleData)\n");
    make_request("GET", BASE_URL "/items/1", NULL, response);
    printf("Response:\n%s\n", response);

    // Test 4: Update Item
    printf("\n[Test] PUT /items/1 (Update Data)\n");
    make_request("PUT", BASE_URL "/items/1", "data=UpdatedData", response);
    printf("Response:\n%s\n", response);

    // Test 5: Retrieve Updated Item
    printf("\n[Test] GET /items/1 (Expect UpdatedData)\n");
    make_request("GET", BASE_URL "/items/1", NULL, response);
    printf("Response:\n%s\n", response);

    // Test 6: Delete Item
    printf("\n[Test] DELETE /items/1\n");
    make_request("DELETE", BASE_URL "/items/1", NULL, response);
    printf("Response:\n%s\n", response);

    // Test 7: Retrieve Deleted Item (Expect Not Found)
    printf("\n[Test] GET /items/1 (Expect Not Found)\n");
    make_request("GET", BASE_URL "/items/1", NULL, response);
    printf("Response:\n%s\n", response);

    // Test 8: Create Multiple Items
    printf("\n[Test] Creating Multiple Items (id=2, id=3)\n");
    make_request("POST", BASE_URL "/items", "id=2&data=DataTwo", response);
    make_request("POST", BASE_URL "/items", "id=3&data=DataThree", response);
    printf("Response:\n%s\n", response);

    // Test 9: List Items Again (Expect 2 Items)
    printf("\n[Test] GET /items (Expect 2 Items)\n");
    make_request("GET", BASE_URL "/items", NULL, response);
    printf("Response:\n%s\n", response);

    // Test 10: Invalid Request (PUT without data)
    printf("\n[Test] PUT /items/2 (Missing Data)\n");
    make_request("PUT", BASE_URL "/items/2", "", response);
    printf("Response:\n%s\n", response);

    // Test 11: Invalid Delete (Item Doesn't Exist)
    printf("\n[Test] DELETE /items/99 (Non-existent Item)\n");
    make_request("DELETE", BASE_URL "/items/99", NULL, response);
    printf("Response:\n%s\n", response);

    printf("\n---- Test Campaign Completed ----\n");
}

int main() {
    run_tests();
    return 0;
}

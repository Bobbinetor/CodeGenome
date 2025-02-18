#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <microhttpd.h>

#define PORT 8888
#define MAX_ITEMS 10
#define DATA_SIZE 256

typedef struct {
    int id;
    char data[DATA_SIZE];
    int active;
} Item;

Item store[MAX_ITEMS];

void init_store() {
    for (int i = 0; i < MAX_ITEMS; i++) {
        store[i].active = 0;
    }
}

int find_index(int id) {
    for (int i = 0; i < MAX_ITEMS; i++) {
        if (store[i].active && store[i].id == id)
            return i;
    }
    return -1;
}

int add_item(int id, const char *data) {
    if (find_index(id) != -1)
        return -1;
    for (int i = 0; i < MAX_ITEMS; i++) {
        if (!store[i].active) {
            store[i].id = id;
            strncpy(store[i].data, data, DATA_SIZE - 1);
            store[i].data[DATA_SIZE - 1] = '\0';
            store[i].active = 1;
            return 0;
        }
    }
    return -2;
}

const char* get_item_data(int id) {
    int index = find_index(id);
    if (index != -1)
        return store[index].data;
    return NULL;
}

int update_item(int id, const char *data) {
    int index = find_index(id);
    if (index == -1)
        return -1;
    strncpy(store[index].data, data, DATA_SIZE - 1);
    store[index].data[DATA_SIZE - 1] = '\0';
    return 0;
}

int delete_item(int id) {
    int index = find_index(id);
    if (index == -1)
        return -1;
    store[index].active = 0;
    return 0;
}

void list_items_str(char *buffer, size_t buffer_size) {
    snprintf(buffer, buffer_size, "Items:\n");
    for (int i = 0; i < MAX_ITEMS; i++) {
        if (store[i].active) {
            char line[300];
            snprintf(line, sizeof(line), "ID: %d, Data: %s\n", store[i].id, store[i].data);
            strncat(buffer, line, buffer_size - strlen(buffer) - 1);
        }
    }
}

struct connection_info_struct {
    char *data;
    size_t size;
};

static enum MHD_Result request_handler(void *cls, struct MHD_Connection *connection,
                                       const char *url, const char *method,
                                       const char *version, const char *upload_data,
                                       size_t *upload_data_size, void **con_cls) {
    if (*con_cls == NULL) {
        struct connection_info_struct *con_info = malloc(sizeof(struct connection_info_struct));
        if (con_info == NULL) {
            return MHD_NO;
        }
        con_info->data = NULL;
        con_info->size = 0;
        *con_cls = con_info;
        return MHD_YES;
    }

    struct connection_info_struct *con_info = *con_cls;

    // Handle incoming POST/PUT data
    if (*upload_data_size != 0) {
        size_t new_size = con_info->size + *upload_data_size;
        char *new_data = realloc(con_info->data, new_size + 1);
        if (new_data == NULL) {
            free(con_info->data);
            free(con_info);
            *con_cls = NULL;
            return MHD_NO;
        }
        memcpy(new_data + con_info->size, upload_data, *upload_data_size);
        new_data[new_size] = '\0';
        con_info->data = new_data;
        con_info->size = new_size;
        *upload_data_size = 0;
        return MHD_YES;
    }

    char response[1024] = "";
    int status_code = MHD_HTTP_OK;

    if (strcmp(method, "GET") == 0) {
        if (strcmp(url, "/items") == 0) {
            list_items_str(response, sizeof(response));
        } else if (strncmp(url, "/items/", 7) == 0) {
            int id = atoi(url + 7);
            const char *data = get_item_data(id);
            if (data) {
                snprintf(response, sizeof(response), "ID: %d, Data: %s", id, data);
                printf("Processing request for item %d\n", id);
            } else {
                snprintf(response, sizeof(response), "Item not found");
                status_code = MHD_HTTP_NOT_FOUND;
                printf("Item %d not found\n", id);
            }
        } else {
            snprintf(response, sizeof(response), "Not found");
            status_code = MHD_HTTP_NOT_FOUND;
        }
    } else if (strcmp(method, "POST") == 0) {
        if (strcmp(url, "/items") == 0) {
            if (con_info->data == NULL) {
                snprintf(response, sizeof(response), "Invalid data");
                status_code = MHD_HTTP_BAD_REQUEST;
                printf("Invalid data\n");
            } else {
                char *id_str = strstr(con_info->data, "id=");
                char *data_str = strstr(con_info->data, "data=");
                if (id_str && data_str) {
                    int id = atoi(id_str + 3);
                    data_str = data_str + 5;
                    int ret = add_item(id, data_str);
                    if (ret == 0) {
                        snprintf(response, sizeof(response), "Item added");
                    } else if (ret == -1) {
                        snprintf(response, sizeof(response), "Item already exists");
                        status_code = MHD_HTTP_BAD_REQUEST;
                    } else {
                        snprintf(response, sizeof(response), "Store full");
                        status_code = MHD_HTTP_SERVICE_UNAVAILABLE;
                    }
                } else {
                    snprintf(response, sizeof(response), "Invalid data");
                    status_code = MHD_HTTP_BAD_REQUEST;
                }
            }
        } else {
            snprintf(response, sizeof(response), "Not found");
            status_code = MHD_HTTP_NOT_FOUND;
        }
    } else if (strcmp(method, "PUT") == 0) {
        if (strncmp(url, "/items/", 7) == 0) {
            int id = atoi(url + 7);
            if (con_info->data == NULL) {
                snprintf(response, sizeof(response), "Invalid data");
                status_code = MHD_HTTP_BAD_REQUEST;
            } else {
                char *data_str = strstr(con_info->data, "data=");
                if (data_str) {
                    data_str = data_str + 5;
                    int ret = update_item(id, data_str);
                    if (ret == 0) {
                        snprintf(response, sizeof(response), "Item updated");
                    } else {
                        snprintf(response, sizeof(response), "Item not found");
                        status_code = MHD_HTTP_NOT_FOUND;
                    }
                } else {
                    snprintf(response, sizeof(response), "Invalid data");
                    status_code = MHD_HTTP_BAD_REQUEST;
                }
            }
        } else {
            snprintf(response, sizeof(response), "Not found");
            status_code = MHD_HTTP_NOT_FOUND;
        }
    } else if (strcmp(method, "DELETE") == 0) {
        if (strncmp(url, "/items/", 7) == 0) {
            int id = atoi(url + 7);
            int ret = delete_item(id);
            if (ret == 0) {
                snprintf(response, sizeof(response), "Item deleted");
            } else {
                snprintf(response, sizeof(response), "Item not found");
                status_code = MHD_HTTP_NOT_FOUND;
            }
        } else {
            snprintf(response, sizeof(response), "Not found");
            status_code = MHD_HTTP_NOT_FOUND;
        }
    } else {
        snprintf(response, sizeof(response), "Method not allowed");
        status_code = MHD_HTTP_METHOD_NOT_ALLOWED;
    }

    struct MHD_Response *mhd_response = MHD_create_response_from_buffer(strlen(response),
                                            (void*)response, MHD_RESPMEM_MUST_COPY);
    int ret_val = MHD_queue_response(connection, status_code, mhd_response);
    MHD_destroy_response(mhd_response);

    if (con_info->data) {
        free(con_info->data);
    }
    free(con_info);
    *con_cls = NULL;
    return ret_val;
}


int main() {
    init_store();
    struct MHD_Daemon *daemon = MHD_start_daemon(MHD_USE_INTERNAL_POLLING_THREAD,
                                                 PORT,
                                                 NULL,
                                                 NULL,
                                                 &request_handler,
                                                 NULL,
                                                 MHD_OPTION_END);
    if (daemon == NULL) {
        fprintf(stderr, "Failed to start server\n");
        return 1;
    }
    printf("Server running on port %d\n", PORT);
    getchar();
    MHD_stop_daemon(daemon);
    return 0;
}

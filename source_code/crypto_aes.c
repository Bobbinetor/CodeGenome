#define _DEFAULT_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <sys/stat.h>
#include <openssl/evp.h>
#include <openssl/rand.h>

#define BUFFER_SIZE 1024

int encrypt_file(const char *in_filename, const char *out_filename, const char *password) {
    FILE *fin = fopen(in_filename, "rb");
    if (!fin) {
        perror("Errore apertura file in lettura");
        return -1;
    }
    FILE *fout = fopen(out_filename, "wb");
    if (!fout) {
        perror("Errore apertura file in scrittura");
        fclose(fin);
        return -1;
    }
    
    unsigned char salt[8];
    if (!RAND_bytes(salt, sizeof(salt))) {
        perror("Errore generazione salt");
        fclose(fin);
        fclose(fout);
        return -1;
    }
    
    // Scrive header "Salted__" seguito dal salt.
    if (fwrite("Salted__", 1, 8, fout) != 8 || fwrite(salt, 1, 8, fout) != 8) {
        perror("Errore scrittura header");
        fclose(fin);
        fclose(fout);
        return -1;
    }
    
    unsigned char key[32], iv[16];
    if (!EVP_BytesToKey(EVP_aes_256_cbc(), EVP_sha256(), salt,
                        (unsigned char*)password, strlen(password), 1, key, iv)) {
        fprintf(stderr, "Errore derivazione chiave\n");
        fclose(fin);
        fclose(fout);
        return -1;
    }
    
    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
    if (!ctx) {
        perror("Errore creazione contesto");
        fclose(fin);
        fclose(fout);
        return -1;
    }
    
    if (EVP_EncryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv) != 1) {
        fprintf(stderr, "Errore inizializzazione crittografia\n");
        EVP_CIPHER_CTX_free(ctx);
        fclose(fin);
        fclose(fout);
        return -1;
    }
    
    unsigned char inbuf[BUFFER_SIZE];
    unsigned char outbuf[BUFFER_SIZE + EVP_CIPHER_block_size(EVP_aes_256_cbc())];
    int inlen, outlen;
    
    while ((inlen = fread(inbuf, 1, BUFFER_SIZE, fin)) > 0) {
        if (EVP_EncryptUpdate(ctx, outbuf, &outlen, inbuf, inlen) != 1) {
            fprintf(stderr, "Errore durante aggiornamento crittografia\n");
            EVP_CIPHER_CTX_free(ctx);
            fclose(fin);
            fclose(fout);
            return -1;
        }
        fwrite(outbuf, 1, outlen, fout);
    }
    
    if (EVP_EncryptFinal_ex(ctx, outbuf, &outlen) != 1) {
        fprintf(stderr, "Errore finale di crittografia\n");
        EVP_CIPHER_CTX_free(ctx);
        fclose(fin);
        fclose(fout);
        return -1;
    }
    fwrite(outbuf, 1, outlen, fout);
    
    EVP_CIPHER_CTX_free(ctx);
    fclose(fin);
    fclose(fout);
    return 0;
}

int decrypt_file(const char *in_filename, const char *out_filename, const char *password) {
    FILE *fin = fopen(in_filename, "rb");
    if (!fin) {
        perror("Errore apertura file in lettura");
        return -1;
    }
    FILE *fout = fopen(out_filename, "wb");
    if (!fout) {
        perror("Errore apertura file in scrittura");
        fclose(fin);
        return -1;
    }
    
    char header[8];
    if (fread(header, 1, 8, fin) != 8) {
        perror("Errore lettura header");
        fclose(fin);
        fclose(fout);
        return -1;
    }
    if (strncmp(header, "Salted__", 8) != 0) {
        fprintf(stderr, "Formato file non valido (header mancante)\n");
        fclose(fin);
        fclose(fout);
        return -1;
    }
    
    unsigned char salt[8];
    if (fread(salt, 1, 8, fin) != 8) {
        perror("Errore lettura salt");
        fclose(fin);
        fclose(fout);
        return -1;
    }
    
    unsigned char key[32], iv[16];
    if (!EVP_BytesToKey(EVP_aes_256_cbc(), EVP_sha256(), salt,
                        (unsigned char*)password, strlen(password), 1, key, iv)) {
        fprintf(stderr, "Errore derivazione chiave\n");
        fclose(fin);
        fclose(fout);
        return -1;
    }
    
    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
    if (!ctx) {
        perror("Errore creazione contesto");
        fclose(fin);
        fclose(fout);
        return -1;
    }
    
    if (EVP_DecryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv) != 1) {
        fprintf(stderr, "Errore inizializzazione decifratura\n");
        EVP_CIPHER_CTX_free(ctx);
        fclose(fin);
        fclose(fout);
        return -1;
    }
    
    unsigned char inbuf[BUFFER_SIZE];
    unsigned char outbuf[BUFFER_SIZE + EVP_CIPHER_block_size(EVP_aes_256_cbc())];
    int inlen, outlen;
    
    while ((inlen = fread(inbuf, 1, BUFFER_SIZE, fin)) > 0) {
        if (EVP_DecryptUpdate(ctx, outbuf, &outlen, inbuf, inlen) != 1) {
            fprintf(stderr, "Errore durante la decifratura\n");
            EVP_CIPHER_CTX_free(ctx);
            fclose(fin);
            fclose(fout);
            return -1;
        }
        fwrite(outbuf, 1, outlen, fout);
    }
    
    if (EVP_DecryptFinal_ex(ctx, outbuf, &outlen) != 1) {
        fprintf(stderr, "Errore finale di decifratura. Verifica la password o il file.\n");
        EVP_CIPHER_CTX_free(ctx);
        fclose(fin);
        fclose(fout);
        return -1;
    }
    fwrite(outbuf, 1, outlen, fout);
    
    EVP_CIPHER_CTX_free(ctx);
    fclose(fin);
    fclose(fout);
    return 0;
}

int main(int argc, char *argv[]) {
    if (argc < 4) {
        printf("Uso: %s <operazione> <cartella> <password>\n", argv[0]);
        printf("Operazioni: enc (cifratura) oppure dec (decifratura)\n");
        return 1;
    }
    
    const char *operation = argv[1];
    const char *folder = argv[2];
    const char *password = argv[3];
    DIR *dir = opendir(folder);
    if (!dir) {
        perror("Errore apertura cartella");
        return 1;
    }
    
    struct dirent *entry;
    char input_path[1024];
    char output_path[1024];
    
    while ((entry = readdir(dir)) != NULL) {
        // Processa solo file regolari.
        if (entry->d_type == DT_REG) {
            snprintf(input_path, sizeof(input_path), "%s/%s", folder, entry->d_name);
            
            if (strcmp(operation, "enc") == 0) {
                snprintf(output_path, sizeof(output_path), "%s/%s.enc", folder, entry->d_name);
                printf("Cifratura del file: %s\n", input_path);
                if (encrypt_file(input_path, output_path, password) != 0) {
                    fprintf(stderr, "Errore durante la cifratura di %s\n", input_path);
                }
            } else if (strcmp(operation, "dec") == 0) {
                // Per evitare conflitti, se il nome termina con ".enc", lo rimuovo per il file decifrato.
                char filename[512];
                strncpy(filename, entry->d_name, sizeof(filename));
                filename[sizeof(filename)-1] = '\0';
                char *dot = strrchr(filename, '.');
                if (dot && strcmp(dot, ".enc") == 0) {
                    *dot = '\0';
                }
                snprintf(output_path, sizeof(output_path), "%s/%s.dec", folder, filename);
                printf("Decifratura del file: %s\n", input_path);
                if (decrypt_file(input_path, output_path, password) != 0) {
                    fprintf(stderr, "Errore durante la decifratura di %s\n", input_path);
                }
            } else {
                printf("Operazione non riconosciuta: %s\n", operation);
                closedir(dir);
                return 1;
            }
        }
    }
    closedir(dir);
    return 0;
}

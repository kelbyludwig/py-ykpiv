#define YKPIV_KEY_SIGNATURE 0x9c
#define YKPIV_ALGO_RSA1024 0x06
#define YKPIV_ALGO_RSA2048 0x07

typedef enum {
  YKPIV_OK = 0,
  YKPIV_MEMORY_ERROR = -1,
  YKPIV_PCSC_ERROR = -2,
  YKPIV_SIZE_ERROR = -3,
  YKPIV_APPLET_ERROR = -4,
  YKPIV_AUTHENTICATION_ERROR = -5,
  YKPIV_RANDOMNESS_ERROR = -6,
  YKPIV_GENERIC_ERROR = -7,
  YKPIV_KEY_ERROR = -8,
  YKPIV_PARSE_ERROR = -9,
  YKPIV_WRONG_PIN = -10,
  YKPIV_INVALID_OBJECT = -11,
  YKPIV_ALGORITHM_ERROR = -12,
  YKPIV_PIN_LOCKED = -13,
  YKPIV_ARGUMENT_ERROR = -14, //i.e. invalid input argument
  YKPIV_RANGE_ERROR = -15, //i.e. value range error
  YKPIV_NOT_SUPPORTED = -16
} ykpiv_rc;

typedef struct ykpiv_state ykpiv_state;

ykpiv_rc ykpiv_init(ykpiv_state **state, int verbose);
ykpiv_rc ykpiv_list_readers(ykpiv_state *state, char *readers, size_t *len);
ykpiv_rc ykpiv_hex_decode(const char *hex_in, size_t in_len, unsigned char *hex_out, size_t *out_len);
ykpiv_rc ykpiv_connect(ykpiv_state *state, const char *wanted);
ykpiv_rc ykpiv_disconnect(ykpiv_state *state);
ykpiv_rc ykpiv_verify(ykpiv_state *state, const char *pin, int *tries);
ykpiv_rc ykpiv_sign_data(ykpiv_state *state, const unsigned char *sign_in, size_t in_len, unsigned char *sign_out, size_t *out_len, unsigned char algorithm, unsigned char key);

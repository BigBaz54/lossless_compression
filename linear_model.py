import message_manager as mm
import math

class LinearModel:
    def compress(self, message):
        # 8 bits for the slope, 
        # 8 bits for the number of bit used for each value,
        # then the errors with the most significant bit to indicate the sign
        compressed_message = ''
        compressed_message += bin(message.mode_param)[2:].zfill(8)
        errors = []
        max_err = 0
        for i in range(message.value_nb):
            expected = message.mode_param*i
            actual = int(message.message[i*message.value_size:(i+1)*message.value_size], 2)
            err = actual-expected
            errors.append(err)
            if abs(err) > max_err:
                max_err = abs(err)
        err_bits = math.ceil(math.log2(max_err))
        compressed_message += bin(err_bits+1)[2:].zfill(8)
        for i in range(message.value_nb):
            e = errors[i]
            compressed_message += ('1' if e<0 else '0')+bin(abs(errors[i]))[2:].zfill(err_bits)
        return compressed_message

    def decompress(self, s):
        slope = int(s[:8], 2)
        err_bits = int(s[8:16], 2)
        received = s[16:]
        max_val = 0
        values = []
        for i in range(len(received)//(err_bits)):
            err_str = received[i*err_bits:(i+1)*err_bits]
            err = int(err_str[1:], 2)*(-1 if err_str[0]=='1' else 1)
            actual_value = slope*i+err
            if abs(actual_value) > max_val:
                max_val = abs(actual_value)
            values.append(actual_value)
        value_size = math.ceil(math.log2(max_val))
        message = ''.join([bin(e)[2:].zfill(value_size) if e>=0 else '0'*value_size for e in values])
        return message
        



if __name__ == '__main__':
    message = mm.LinearBinaryMessage(1000, mode_param = 2, max_error = 5)
    model = LinearModel()
    compressed_message = model.compress(message)
    decompressed_message = model.decompress(compressed_message)
    print(f'\nCorrect ? {message.message == decompressed_message}')
    print(f'\nInitial message size: {len(message.message)}\nCompressed message size: {len(compressed_message)}\nCompression ratio: {len(compressed_message)/len(message.message)}\n')
import message_manager as mm
import math

class RecurrenceModel:
    def compress(self, message):
        # 16 bits for the first value,
        # 8 bits for the number of bits used for each value,
        # then the steps with the most significant bit to indicate the sign
        compressed_message = ''
        compressed_message += bin(message.first)[2:].zfill(16)
        steps = []
        max_step = 0
        u = message.first
        for i in range(1, message.value_nb+1):
            u1_str = message.message[i*message.value_size:(i+1)*message.value_size]
            u1 = (-1 if u1_str[0]=='1' else 1)*int(u1_str[1:], 2)
            step = u1-u
            steps.append(step)
            if abs(step) > max_step:
                max_step = abs(step)
            u = u1
        step_bits = math.floor(math.log2(max_step))+1+1
        compressed_message += bin(step_bits)[2:].zfill(8)
        for i in range(message.value_nb):
            e = steps[i]
            compressed_message += ('1' if e<0 else '0')+bin(abs(steps[i]))[2:].zfill(step_bits-1)
        return compressed_message

    def decompress(self, s):
        u = int(s[:16], 2)
        step_bits = int(s[16:24], 2)
        received = s[24:]
        max_val = 0
        values = [u]
        value_nb = len(received)//step_bits
        for i in range(value_nb):
            step_str = received[i*step_bits:(i+1)*step_bits]
            step = int(step_str[1:], 2)*(-1 if step_str[0]=='1' else 1)
            u1 = u+step
            if abs(u1) > max_val:
                max_val = abs(u1)
            values.append(u1)
            u = u1
        value_size = (math.floor(math.log2(max_val))+1)+1
        message = ''.join([('0' if e>=0 else '1') + bin(abs(e))[2:].zfill(value_size-1) for e in values])
        return message
        



if __name__ == '__main__':
    message = mm.RecurrenceBinaryMessage(1000, max_step = 3)
    model = RecurrenceModel()
    compressed_message = model.compress(message)
    decompressed_message = model.decompress(compressed_message)
    print(f'\nCorrect ? {message.message == decompressed_message}')
    print(f'\nInitial message size: {len(message.message)}\nCompressed message size: {len(compressed_message)}\nCompression ratio: {len(compressed_message)/len(message.message)}\n')

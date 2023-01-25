import generate_message

def create_message_binary(length, path):
    with open(path, 'w') as f:
        f.write(generate_message.generate_binary(length))
    
def create_message_alphanumeric(length, path):
    with open(path, 'w') as f:
        f.write(generate_message.generate_alphanumeric(length))

if __name__ == '__main__':
    create_message_alphanumeric(10000, 'msg.txt')
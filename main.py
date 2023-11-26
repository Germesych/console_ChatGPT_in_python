import g4f
import subprocess

context = ''
pattern = ''
question = ''


start_session = """
######################
#         Hi!        #
#  ChatGPT 3.5turbo  #
######################
"""

end_session = """
######################
#    bye-bye...      #
#  See you later. ;) #
######################
"""


def python_version():
    result = subprocess.run(['python3', '--version'], capture_output=True, text=True)

    if result.returncode == 0:
        output = result.stdout.strip()
        if int(output.split(".")[1]) > 9:
            return True
        print(f"Ваша версия Python 3 ниже 3.10: {output}")
        return False
    else:
        # Обработка случая, когда команда завершилась с ошибкой
        error = result.stderr.strip()
        print("По умолчанию будет использоваться Python 3.10...\n")
        print(error)


def get_chat(message: str = '') -> str:
    message = [
        {
            "role": "system",
            "content": pattern
        },
        {
            "role": "assistant",
            "content": context
        },
        {
            "role": "user",
            "content": message
        }
    ]
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_35_turbo,
            messages=message
        )
        return response
    except Exception as e:
        print('Sorry Error request')


def chat_menu(value):
    pass
#     match value:
#         case "1":
#             result()


def main():
    # get_chat(question)
    global question
    input_text = input("Введите свой запрос:")
    input_menu = input("Введите свой ответ:")
    menu = "[1] задать еще вопрос | [2] Продолжить беседу | [3] выйти из чата"

    if python_version():
        if input_text != '':
            question = input_text
            print(get_chat(question))
            print(f"\n\n{menu}")
            print(input_menu)


if __name__ == '__main__':
    if python_version():
        main()



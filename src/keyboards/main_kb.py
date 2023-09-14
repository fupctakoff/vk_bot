from vk_api.keyboard import VkKeyboard, VkKeyboardColor


main_keyboard = VkKeyboard()
main_keyboard.add_button(label='погода')
main_keyboard.add_button(label='пробка')
main_keyboard.add_button(label='афиша')
main_keyboard.add_button(label='валюта')


print(main_keyboard.__dir__())
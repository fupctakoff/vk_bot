from vk_api.keyboard import VkKeyboard, VkKeyboardColor

main_keyboard = VkKeyboard()
main_keyboard.add_button(label='погода')
main_keyboard.add_button(label='пробка')
main_keyboard.add_line()
main_keyboard.add_button(label='афиша')
main_keyboard.add_button(label='валюта')
main_keyboard.add_line()
main_keyboard.add_button(label='сменить город', color=VkKeyboardColor.POSITIVE)

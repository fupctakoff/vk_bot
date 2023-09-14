from vk_api.keyboard import VkKeyboard, VkKeyboardColor

support_keyboard = VkKeyboard()
support_keyboard.add_button(label='сегодня')
support_keyboard.add_button(label='завтра')
support_keyboard.add_line()
support_keyboard.add_button(label='назад', color=VkKeyboardColor.NEGATIVE)

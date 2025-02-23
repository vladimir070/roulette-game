def play_roulette():
    """
    Простая игра в рулетку без использования модулей.
    """

    player_points = 100
    game_over = False

    def get_player_bet():
        """
        Получает ставку игрока: число и цвет.
        """
        while True:
            try:
                number = int(input("Введите число (0-36): "))
                if 0 <= number <= 36:
                    break
                else:
                    print("Неверный ввод. Число должно быть от 0 до 36.")
            except ValueError:
                print("Неверный ввод. Введите целое число.")

        while True:
            color = input("Введите цвет (красное/черное/зеленое): ").lower()
            if color in ("красное", "черное", "зеленое"):
                break
            else:
                print("Неверный ввод. Цвет должен быть красное, черное или зеленое.")

        return number, color

    def spin_roulette():
        """
        Генерирует случайное число и цвет рулетки.
        """
        # Эмулируем случайность простым способом (не идеально, но без модулей):
        import time # Импортируем модуль time только для функции random
        random_seed = int(str(time.time()).replace('.', '')) % 37 #  генерируем "случайное" число на основе текущего времени.
                                                        #   Это не настоящий случайный генератор, а простой способ получить
                                                        #   псевдослучайное число без импорта модуля `random`.
        time.sleep(0.01)  # небольшая задержка, чтобы seed менялся чаще
        number = random_seed
        # Цвета рулетки (упрощенно):
        red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

        if number == 0:
            color = "зеленое"
        elif number in red_numbers:
            color = "красное"
        else:
            color = "черное"

        return number, color

    def determine_winner(player_number, player_color, roulette_number, roulette_color):
        """
        Определяет, выиграл ли игрок.
        """
        if player_number == roulette_number and player_color == roulette_color:
            return True
        else:
            return False

    def update_points(winner, current_points):
        """
        Обновляет очки игрока.
        """
        if winner:
            return current_points + 10
        else:
            return current_points - 10

    def print_game_status(roulette_number, roulette_color, points):
        """
        Выводит результаты раунда и текущее количество очков.
        """
        print(f"Выпало: {roulette_number} {roulette_color}")
        print(f"У вас {points} очков.")

    # Основной игровой цикл
    while not game_over:
        print(f"\nУ вас {player_points} очков.")
        if player_points <= 0:
            print("У вас закончились очки. Вы проиграли!")
            game_over = True
            continue # Завершаем цикл, если нет очков

        number, color = get_player_bet()
        roulette_number, roulette_color = spin_roulette()
        winner = determine_winner(number, color, roulette_number, roulette_color)
        player_points = update_points(winner, player_points)
        print_game_status(roulette_number, roulette_color, player_points)

        if player_points <= 0:
            print("У вас закончились очки. Вы проиграли!")
            game_over = True
        else:
            play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
            if play_again != "да":
                game_over = True
                print("Спасибо за игру!")

# Запуск игры
play_roulette()
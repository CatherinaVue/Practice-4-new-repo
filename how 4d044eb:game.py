[33mcommit 4d044eb60c3510709f49fcd62c22a563eadefc67[m
Author: Carson-Hahn <chahn8626@floridapoly.edu>
Date:   Thu Nov 13 00:51:50 2025 +0000

    Add computer rand response

[1mdiff --git a/game.py b/game.py[m
[1mindex 6aa554d..fb5db69 100644[m
[1m--- a/game.py[m
[1m+++ b/game.py[m
[36m@@ -1,7 +1,8 @@[m
 import random[m
 [m
[31m-choices = ["rock", "paper", "scissors"][m
[31m-computer_choice = random.choice(choices)[m
[32m+[m[32mdef computer_choice():[m
[32m+[m[32m    options = ["rock", "paper", "scissors"][m
[32m+[m[32m    return random.choice(options)[m
 [m
[31m-print("Welcome to Rock-Paper-Scissors!")[m
[31m-print(f"Computer chose: {computer_choice}")[m
\ No newline at end of file[m
[32m+[m[32mif __name__ == "__main__":[m
[32m+[m[32m    print("Computer chooses:", computer_choice())[m
\ No newline at end of file[m

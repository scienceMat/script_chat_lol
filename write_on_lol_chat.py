import time
import pyautogui
import pyperclip
# Attendez que l'utilisateur soit prêt à effectuer la recherche sur YouTube.
input("Appuyez sur Entrée lorsque vous êtes prêt à commencer...")
time.sleep(2)
# Capturez l'emplacement du chat lol 
x, y = pyautogui.locateCenterOnScreen('chat_lol.png', confidence=0.8)

if x is not None and y is not None:
    print(f"Barre de recherche trouvée aux coordonnées : x = {x}, y = {y}")
    
    # Cliquez sur l'input du chat pour y entrer du texte.
    pyautogui.click(x, y)
    
    # Écrivez le texte que vous souhaitez mettre
    texte_a_envoyer = "Hey team, let's stay positive and keep up the good vibes – we've got this! 🏆"
    pyautogui.write(texte_a_envoyer)
    discord = "https://discord.gg/JuXgWxWR , to be more coordinated🎤"
    # Appuyez sur la touche "Enter" pour lancer la recherche.
    pyautogui.press('enter')
    pyperclip.copy(discord)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

    
else:
    print("Barre de recherche non trouvée sur l'écran.")

# Attendez quelques secondes pour voir les résultats de la recherche.
time.sleep(5)
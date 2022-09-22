# Importes 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Seleccionar el WebDriver y definir la URL
d = webdriver.Chrome(executable_path=r"C:\Users\ianve\Documents\Universidad\7 Semestre\Calidad de Software\chromedriver.exe")
d.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
d.maximize_window() # Maximizar Ventana

# Se definen los nombres de los ID de los objetos target y source
sources = ["box1", "box2", "box3", "box4", "box5", "box6", "box7"]
targets = ["box101", "box102", "box103", "box104", "box105", "box106", "box107"]

# Se itera sobre la cantidad de elementos para realizar las acciones
for i in range(0, 7):
    source = d.find_element(By.ID, sources[i])
    target = d.find_element(By.ID, targets[i])
    ActionChains(d).drag_and_drop(source, target).perform()

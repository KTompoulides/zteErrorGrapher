from selenium import webdriver
import time
import matplotlib.animation as animation
import datetime as dt
import matplotlib.pyplot as plt
import sys
# initiate

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
fe = ""


# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

    upt = driver.find_element("xpath", "/html/body/div[3]/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[1]/div[2]/div[2]/form/div[13]/span[2]")
    showtime = upt.get_attribute("innerHTML")
    fecErr = driver.find_element("xpath","/html/body/div[3]/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[1]/div[2]/div[2]/form/div[16]/span[2]")
    fe = fecErr.get_attribute("innerHTML")
    button = driver.find_element("xpath", "/html/body/div[3]/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[1]/div[2]/div[4]/input")
    button.click()
    print(showtime,"////",fe)

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S'))
    ys.append(fe[2:])

    # Limit x and y lists to 20 items
    xs = xs[-50:]
    ys = ys[-50:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('FEC Errors over time')
    plt.ylabel('FEC Errors')


if(len(sys.argv)<5):
    print("Invalid arguments!\nTo run type python3 zteErrorGrapher.py router_ip username password refresh_interval")
    exit(-1)
gatewayAddress = sys.argv[1]
loginUser = sys.argv[2]
loginPass = sys.argv[3]
interval = sys.argv[4]
fullAddress = "http://" + gatewayAddress
driver = webdriver.Firefox()
driver.get(fullAddress) # go to the url

username_field = driver.find_element("name", "Frm_Username")
password_field = driver.find_element("name", "Frm_Password")

# log in
username_field.send_keys(loginUser) # enter in your username
password_field.send_keys(loginPass) # enter in your password
button = driver.find_element("xpath","/html/body/div[3]/div[3]/div/div[3]/input")
button.click()
button = driver.find_element("xpath","/html/body/div[3]/div[2]/div[2]/div[2]/ul/li[2]/a")
button.click()

ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=5000)
plt.show()

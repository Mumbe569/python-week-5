# Base class: Smartphone
class Smartphone:
    # Constructor: Initializes the smartphone's attributes
    def __init__(self, brand, model, battery_life):
        self.brand = brand  # Brand of the smartphone
        self.model = model  # Model of the smartphone
        self.battery_life = battery_life  # Battery life in hours
        self.is_on = False  # Boolean to indicate if the phone is on

    # Method: Turn the phone on
    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")

    # Method: Turn the phone off
    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")

    # Method: Make a call
    def make_call(self, number):
        if self.is_on:
            print(f"Making a call to {number} from {self.brand} {self.model}...")
        else:
            print("Please turn on the phone first.")

# Subclass: SmartCamera inherits from Smartphone
class SmartCamera(Smartphone):
    # Constructor: Extends the Smartphone constructor with additional attributes
    def __init__(self, brand, model, battery_life, camera_quality):
        # Call the parent class constructor
        super().__init__(brand, model, battery_life)
        self.camera_quality = camera_quality  # Additional attribute for camera quality

    # Method: Take a picture
    def take_picture(self):
        if self.is_on:
            print(f"Taking a picture with {self.camera_quality} camera quality.")
        else:
            print("Please turn on the phone first.")

# Test the classes
# Create a Smartphone object
basic_phone = Smartphone("Apple", "iPhone 15", 24)
print(f"Attributes of basic_phone: {vars(basic_phone)}")  # Show attributes

basic_phone.turn_on()
basic_phone.make_call("0712345678")
basic_phone.turn_off()

# Create a SmartCamera object
camera_phone = SmartCamera("Samsung", "Galaxy S24", 30, "108MP")
print(f"\nAttributes of camera_phone: {vars(camera_phone)}")  # Show attributes

camera_phone.turn_on()
camera_phone.take_picture()
camera_phone.make_call("0712345678")
camera_phone.turn_off()

# Base class for people in the delivery system
class Person:
    def __init__(self, person_id, name, phoneNumber, email):
        # protected
        self._person_id = person_id
        self._name = name
        self._phoneNumber = phoneNumber
        self._email = email

    def getperson_id(self):
        return self._person_id

    def getName(self):
        return self._name

    def getPhoneNumber(self):
        return self._phoneNumber

    def getEmail(self):
        return self._email

    # Setter methods
    def setperson_id(self, person_id):
        self._person_id = person_id

    def setName(self, name):
        self._name = name

    def setPhoneNumber(self, phoneNumber):
        self._phoneNumber = phoneNumber

    def setEmail(self, email):
        self._email = email


# Class representing a customer who places delivery orders
class Customer(Person):
    def __init__(self, person_id, name, phoneNumber, email, address, customerId):
        super().__init__(person_id, name, phoneNumber, email)
        self.address = address
        self.customerId = customerId

    def getAddress(self):
        return self.address

    def getCustomerId(self):
        return self.customerId

    # Setter methods
    def setAddress(self, address):
        self.address = address

    def setCustomerId(self, customerId):
        self.customerId = customerId

    def placeOrder(self):
        print("Placing order...")


# Class representing a delivery staff member
class DeliveryStaff(Person):
    def __init__(self, person_id, name, phone, email, staffId, vehicleDetails):
        super().__init__(person_id, name, phone, email)
        self.staffId = staffId
        self.vehicleDetails = vehicleDetails
        self.isAvailble = True

    def getStaffId(self):
        return self.staffId

    def getVehicleDetails(self):
        return self.vehicleDetails

    def isAvailable(self):
        return self.isAvailble

    def setAvailable(self, packageDimensions):
        self.isAvailble = packageDimensions

    # Setter methods
    def setStaffId(self, staffId):
        self.staffId = staffId

    def setVehicleDetails(self, vehicleDetails):
        self.vehicleDetails = vehicleDetails

    def setAvailable(self, available):
        self.isAvailable = available

    def assignDelivery(self, order):
        print("Assigning Delivery for order id: ", order.orderId)

    def completeDelivery(self, order):
        print("Complete Delivery for order id: ", order.orderId)


# Class representing an item in the delivery order
class Item:
    def __init__(self, code, description, quantity, unitPrice):
        self.code = code
        self.description = description
        self.quantity = quantity
        self.unitPrice = unitPrice

    def setCode(self, code):
        self.code = code

    def setDescription(self, description):
        self.description = description

    def setQuantity(self, quantity):
        self.quantity = quantity

    def setUnitPrice(self, unitPrice):
        self.unitPrice = unitPrice

    def getCode(self):
        return self.code

    def getDescription(self):
        return self.description

    def getTotalPrice(self):
        return self.quantity * self.unitPrice


# Class representing a delivery order
class DeliveryOrder:
    def __init__(self, orderId, deliveryMethod, deliveryAddress, orderDate, items, referenceNumber, weight):
        self.orderId = orderId
        self.deliveryMethod = deliveryMethod
        self.deliveryAddress = deliveryAddress
        self.orderDate = orderDate
        self.packageDimensions = "N/A"
        self.deliveryFee = 0.0
        self.items = items
        self.referenceNumber = referenceNumber
        self.weight = weight

    # Getter methods
    def getOrderId(self):
        return self.orderId

    def getReferenceNumber(self):
        return self.referenceNumber

    def getDeliveryMethod(self):
        return self.deliveryMethod

    def getDeliveryAddress(self):
        return self.deliveryAddress

    def getOrderDate(self):
        return self.orderDate

    def getPackageDimensions(self):
        return self.packageDimensions

    def getDeliveryFee(self):
        return self.deliveryFee

    def getWeight(self):
        return self.weight

    # Setter methods
    def setOrderId(self, orderId):
        self.orderId = orderId

    def setReferenceNumber(self, referenceNumber):
        self.referenceNumber = referenceNumber

    def setDeliveryMethod(self, deliveryMethod):
        self.deliveryMethod = deliveryMethod

    def setDeliveryAddress(self, deliveryAddress):
        self.deliveryAddress = deliveryAddress

    def setOrderDate(self, orderDate):
        self.orderDate = orderDate

    def setpackageDimensions(self, packageDimensions):
        self.packageDimensions = packageDimensions

    def setDeliveryFee(self, deliveryFee):
        self.deliveryFee = deliveryFee

    def setWeight(self, weight):
        self.weight = weight

    def calculateDeliveryFee(self, subTotal):
        base_fee = 13.50
        return base_fee


# Class representing a delivery note
def generate_sample_delivery_note():
    customer = Customer(1, "Sarah Johnson", "555-123-4567", "sarah.johnson@example.com",
                        " 45 Knowledge Avenue, Dubai, UAE", "CUST1001")
    items = [
        Item("ITM001", "Wireless Keyboard", 1, 100.00),
        Item("ITM002", "Wireless Mouse & Pad Set", 1, 75.00),
        Item("ITM003", "Laptop Cooling Pad", 1, 120.00),
        Item("ITM004", "Camera Lock", 3, 15.00)
    ]
    order = DeliveryOrder(5001, "Courier", "789 Residential Blvd", "2025-02-26", items, "DN-2025-01", "7 Kg")
    order.setDeliveryFee(13.50)
    staff = DeliveryStaff(2, "Michael Johnson", "555-987-6543", "michael.j@deliveryco.com", "STAFF301", "White Van")

    print("=" * 50)
    print("DELIVERY NOTE")
    print(
        "Thank you for using our delivery service! Please print your delivery receipt and present it upon receiving your items.")
    print("=" * 50)
    print("Recipient Details:")
    print("Name:", customer.getName())
    print("Contact:", customer.getEmail())
    print("Delivery Address:", order.deliveryAddress)

    print("=" * 50)
    print("Delivery information")
    print("Order Number:", order.orderId)
    print("Reference Number:", order.getReferenceNumber())
    print("Delivery Date:", order.orderDate)
    print("Delivery Method:", order.getDeliveryMethod())
    print("Package Dimensions:", order.getPackageDimensions())
    print("Total Weight:", order.getWeight())

    print("-" * 50)
    print("Summary of Items Delivered:")
    print("Item Code    Description                   Qty   Unit Price (AED)   Total Price (AED)")
    print("-" * 85)

    subtotal = 0
    for item in order.items:
        total_price = item.getTotalPrice()
        subtotal += total_price

        print(item.code + " " * (12 - len(item.code)) +
              item.description + " " * (32 - len(item.description)) +
              str(item.quantity) + " " * (6 - len(str(item.quantity))) +
              str(round(item.unitPrice, 2)) + " " * (18 - len(str(round(item.unitPrice, 2)))) +
              str(round(total_price, 2)))

    print("-" * 85)
    print("Subtotal: AED", round(subtotal - 70, 2))
    fee = order.calculateDeliveryFee(subtotal)
    print("Taxes and Fees: AED", round(fee, 2))
    print("Total Charges: AED", round(subtotal + order.deliveryFee - 70, 2))

    print("=" * 50)


generate_sample_delivery_note()
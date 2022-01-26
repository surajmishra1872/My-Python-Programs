
print("नमस्ते कोरोना वायरस संक्रमण सॉफ्टवेयर में आपका स्वागत है| बताइए अपने लक्षणों को जानें अपना इलाज")
data=[]
print( "\n\nकोरोना वायरस- कोरोना वायरस का संबंध वायरस के ऐसे परिवार से है, जिसके संक्रमण से जुकाम से लेकर सांस लेने में तकलीफ जैसी समस्या हो सकती है. इस वायरस को पहले कभी नहीं देखा गया है. इस वायरस का संक्रमण दिसंबर में चीन के वुहान में शुरू हुआ था. डब्लूएचओ के मुताबिक, बुखार, खांसी, सांस लेने में तकलीफ इसके लक्षण हैं. अब तक इस वायरस को फैलने से रोकने वाला कोई टीका नहीं बना है.")
name=input("\n\nENTER YOUR name")
data.append(name)
age=int(input("ENTER YOUR AGE"))
data.append(age)
tempreture=float(input("\nENTER YOUR TEMPRETURE"))
if tempreture <=37:
   print("\nYOU HAVE NO FEVER")
kharas = input("\nKYA AAPKO KHARAS HAI")
if kharas=="yes":
    khaasi=input("\nKYA AAPKO KHAASI HAI")
elif kharas=="no":
    khaasi=input("\nKYA AAPKO KHAASI HAI")
if khaasi=="yes":
    sans=input("\nKYA AAPKO SANS LENE MAI PROBLEM HAI")
elif khaasi=="no":
    sans=input("\nKYA AAPKO SANS LENE MAI PROBLEM HAI")
if sans=="yes":
    sir=input("\nKYA AAPKE SIR MAI DARD HAI")
elif sans=="no": 
    sir=input("\nKYA AAPKE SIR MAI DARD HAI")   
if sir=="yes":
   thakan=input("\nKYA AAPKO THAKAN BHI HO RHI HAI")
elif sir=="no":
    thakan=input("\nKYA AAPKO THAKAN BHI HO RHI HAI")
if thakan=="yes":
   print("\nARE YOU WANT TO VIEW YOUR RESULT")
elif thakan=="no":
    result=input("\nARE YOU  WANT TO VIEW YOUR RESULT")
    if result=="yes":
       print(f"your name is {name} and age is {age}")
       print("\n\nकोरोना के लक्षण - इसके लक्षण फ्लू से मिलते-जुलते हैं. संक्रमण के फलस्वरूप बुखार, जुकाम, सांस लेने में तकलीफ, नाक बहना और गले में खराश जैसी समस्या उत्पन्न होती हैं. यह वायरस एक व्यक्ति से दूसरे व्यक्ति में फैलता है. इसलिए इसे लेकर बहुत सावधानी बरती जा रही है. कुछ मामलों में कोरोना वायरस घातक भी हो सकता है. खास तौर पर अधिक उम्र के लोग और जिन्हें पहले से अस्थमा, डायबिटीज़ और हार्ट की बीमारी है.")
       print("\n STAY AT HOME")
       print("\n\nटेस्ट करने के लिए धन्यवाद")
    elif result=="no":
         print("\nटेस्ट करने के लिए धन्यवाद")
         print("\nSTAY AT HOME")
    

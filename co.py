
print("Namaste CORONA VIRUS Sankraman TESTING SOFTWARE Mein Aapaka Svaagat Hai Bataie Apane Lakshanon Ko Jaanen Apana ILaaj")
data=[]
chek=[]
print( "\n\nCORONA  VIRUS Parichay - Korona Vaayaras Ka Sambandh Vaayaras Ke Aise Parivaar Se Hai, Jisake Sankraman Se Jukaam Se Lekar Saans Lene Mein Takaleeph Jaisee Samasya Ho Sakatee Hai. Is Vaayaras Ko Pahale Kabhee Nahin Dekha Gaya Hai. Is Vaayaras Ka Sankraman Disambar Mein Cheen Ke Vuhaan Mein Shuroo Hua Tha. Dablooecho Ke Mutaabik, Bukhaar, Khaansee, Saans Lene Mein Takaleeph Isake Lakshan Hain. Ab Tak Is Vaayaras Ko Phailane Se Rokane Vaala Koee Teeka Nahin Bana Hai.")
name=input("\n\nENTER YOUR NAME")
data.append(name)
age=int(input("ENTER YOUR AGE"))
data.append(age)
tempreture=float(input("\nENTER YOUR TEMPRETURE "))
if tempreture <=37:
   print("\nYOU HAVE NO FEVER")
   print("\n\nPLEASE GIVE YOUR ANSWER IS SMALL LETTER LIKE AS-yes,no")
else:
   print("YOU HAVE FEVER")
   print("\n\nPLEASE GIVE YOUR ANSWER IS SMALL LETTER LIKE AS-yes,no")
kharas = input("\nKYA AAPKO KHARAS HAI")
chek.append(kharas)
if kharas=="yes":
    khaasi=input("\nKYA AAPKO KHAASI HAI")
    chek.append(khaasi)
elif kharas=="no":
    khaasi=input("\nKYA AAPKO KHAASI HAI")
    chek.append(khaasi)
if khaasi=="yes":
    sans=input("\nKYA AAPKO SANS LENE MAI PROBLEM HAI")
    chek.append(sans)
elif khaasi=="no":
    sans=input("\nKYA AAPKO SANS LENE MAI PROBLEM HAI")
    chek.append(sans)
if sans=="yes":
    sir=input("\nKYA AAPKE SIR MAI DARD HAI")
    chek.append(sir)
elif sans=="no": 
    sir=input("\nKYA AAPKE SIR MAI DARD HAI")
    chek.append(sir)
if sir=="yes":
   thakan=input("\nKYA AAPKO THAKAN BHI HO RHI HAI")
   chek.append(thakan)
elif sir=="no":
    thakan=input("\nKYA AAPKO THAKAN BHI HO RHI HAI")
    chek.append(thakan)
if thakan=="yes":
   
    result = input("\nARE YOU WANT TO VIEW YOUR RESULT")
elif thakan=="no":
    result=input("\nARE YOU  WANT TO VIEW YOUR RESULT")
if result=="yes":
   a=all([i=="yes" for i in chek])
   if a==True:
       print(f"\n\nCOVID -19 PATENT DETAILS \n\n\n YOUR NAME IS {name} & AGE IS {age} & YOUR BODY TEMPRETURE IS -:{tempreture}")
       print("\n\nAapake Test Mein CORONA Ke Lakshan Pae Gae Hain Kripaya DOCTER Se Milie")
       print("\n\nKorona Ke Lakshan :-  Isake Lakshan Phloo Se Milate-Julate Hain. Sankraman Ke Phalasvaroop Bukhaar, Jukaam, Saans Lene Mein Takaleeph, Naak Bahana Aur Gale Mein Kharaash Jaisee Samasya Utpann Hotee Hain. Yah Vaayaras Ek Vyakti Se Doosare Vyakti Mein Phailata Hai. Isalie Ise Lekar Bahut Saavadhaanee Baratee Ja Rahee Hai. Kuchh Maamalon Mein Korona Vaayaras Ghaatak Bhee Ho Sakata Hai. Khaas Taur Par Adhik Umr Ke Log Aur Jinhen Pahale Se Asthama, Daayabiteez Aur Haart Kee Beemaaree Hai.")
       print("\n STAY AT HOME STAY SAFE")
       print("\n\nTest Karane Ke Lie Dhanyavaad")
       print("\n SOFTWARE HAS DEVLOPED BY -SURAJ KUMAR MISHRA")
   else:
      print("\n\n\nGhabaraie Mat Aapako CORONA VIRUS Nahin Hua Hai Kripaya Ghar Mein Rahie Ghar Par Rahie Surakshit Rahie")
      print("\n\n CORONA VIRUS Ke Lakshan - Isake Lakshan Phloo Se Milate-Julate Hain. Sankraman Ke Phalasvaroop Bukhaar, Jukaam, Saans Lene Mein Takaleeph, Naak Bahana Aur Gale Mein Kharaash Jaisee Samasya Utpann Hotee Hain. Yah Vaayaras Ek Vyakti Se Doosare Vyakti Mein Phailata Hai. Isalie Ise Lekar Bahut Saavadhaanee Baratee Ja Rahee Hai. Kuchh Maamalon Mein Korona Vaayaras Ghaatak Bhee Ho Sakata Hai. Khaas Taur Par Adhik Umr Ke Log Aur Jinhen Pahale Se Asthama, Daayabiteez Aur Haart Kee Beemaaree Hai.")
      print("\n\nThank You For Testing")
      print("\n SOFTWARE HAS DEVLOPED BY -SURAJ KUMAR MISHRA")
else:
   
   print("\nThank You For Testing")
   print("\nSTAY AT HOME , STAY SAFE")
   print("\n\n CORONA VIRUS Ke Lakshan - Isake Lakshan Phloo Se Milate-Julate Hain. Sankraman Ke Phalasvaroop Bukhaar, Jukaam, Saans Lene Mein Takaleeph, Naak Bahana Aur Gale Mein Kharaash Jaisee Samasya Utpann Hotee Hain. Yah Vaayaras Ek Vyakti Se Doosare Vyakti Mein Phailata Hai. Isalie Ise Lekar Bahut Saavadhaanee Baratee Ja Rahee Hai. Kuchh Maamalon Mein Korona Vaayaras Ghaatak Bhee Ho Sakata Hai. Khaas Taur Par Adhik Umr Ke Log Aur Jinhen Pahale Se Asthama, Daayabiteez Aur Haart Kee Beemaaree Hai.")
   print("\n SOFTWARE HAS DEVLOPED BY -SURAJ KUMAR MISHRA")  

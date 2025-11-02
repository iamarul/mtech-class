# chatbot_logic.py

def get_response(user_input):
    user_input = user_input.lower()

    if 'admission' in user_input or 'apply' in user_input:
        return "You can apply online at https://www.srmist.edu.in. Admissions are based on SRMJEEE or qualifying exam scores."

    elif 'course' in user_input or 'program' in user_input:
        return "SRM offers B.Tech, M.Tech, MBA, B.Sc, M.Sc, BBA, and more across Engineering, Management, Science, and Humanities."

    elif 'eligibility' in user_input:
        return "For B.Tech, candidates must have passed 10+2 with Physics, Chemistry, and Mathematics. For MBA, a Bachelor’s degree with at least 50% marks is required."

    elif 'fee' in user_input or 'fees' in user_input:
        return "Fees vary by program. For B.Tech, it ranges between ₹2.5–3.5 lakhs per year. Check the official website for details."

    elif 'scholarship' in user_input:
        return "SRM offers scholarships based on merit, SRMJEEE rank, sports achievements, and socio-economic status."

    elif 'hostel' in user_input or 'accommodation' in user_input:
        return "SRM provides modern hostels for boys and girls with Wi-Fi, mess, laundry, and recreational facilities."

    elif 'campus' in user_input or 'location' in user_input:
        return "SRM has campuses in Kattankulathur (Chennai), Ramapuram, Vadapalani, Delhi-NCR, Amaravati, and Sonepat."

    elif 'contact' in user_input or 'phone' in user_input or 'email' in user_input:
        return "You can reach the SRM Admission Office at +91-44-2745 5510 or email admissions@srmist.edu.in."

    elif 'placement' in user_input:
        return "SRM has an excellent placement record with recruiters like Amazon, Microsoft, TCS, and Infosys offering top packages."

    elif 'bye' in user_input or 'exit' in user_input or 'thank' in user_input:
        return "Thank you for your interest in SRM! Have a great day! 👋"

    else:
        return "I'm sorry, I don’t have information on that. Please visit https://www.srmist.edu.in for more details."

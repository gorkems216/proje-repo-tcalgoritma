import tkinter as tk
from tkinter import messagebox
import random

class TCKimlikDogrulama(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TC Kimlik Numarası Doğrulama")
        self.geometry("450x350")
        # Türk bayrağının ana rengini kullan
        self.configure(bg="#E30A17")  # Kırmızı
        
        # Ana çerçeve
        frame = tk.Frame(self, bg='white', bd=5)
        frame.place(relx=0.5, rely=0.5, anchor='center', width=350, height=250)
        
        # Başlık
        title_label = tk.Label(frame, text="TC Kimlik Numarası Doğrulama", font=("Arial", 14, "bold"), bg='white')
        title_label.pack(pady=15)
        
        # Giriş alanı çerçevesi
        input_frame = tk.Frame(frame, bg='white')
        input_frame.pack(pady=10)
        
        # TC kimlik giriş etiketi ve alanı
        tc_label = tk.Label(input_frame, text="TC Kimlik No:", font=("Arial", 12), bg='white')
        tc_label.grid(row=0, column=0, padx=5)
        
        self.tc_entry = tk.Entry(input_frame, font=("Arial", 12), width=15)
        self.tc_entry.grid(row=0, column=1, padx=5)
        
        # Butonlar için çerçeve
        button_frame = tk.Frame(frame, bg='white')
        button_frame.pack(pady=20)
        
        # Doğrulama butonu
        self.verify_button = tk.Button(button_frame, text="Doğrula", command=self.verify_tc,
                                       bg='#E30A17', fg='white', font=("Arial", 10, "bold"),
                                       width=10, height=1)
        self.verify_button.grid(row=0, column=0, padx=10)
        
        # Temizle butonu
        self.clear_button = tk.Button(button_frame, text="Temizle", command=self.clear_entry,
                                      bg='#2A2A2A', fg='white', font=("Arial", 10, "bold"),
                                      width=10, height=1)
        self.clear_button.grid(row=0, column=1, padx=10)
        
        # Rastgele TC üret butonu
        self.random_button = tk.Button(button_frame, text="Rastgele TC", command=self.generate_random_tc,
                                      bg='#2A2A2A', fg='white', font=("Arial", 10, "bold"),
                                      width=10, height=1)
        self.random_button.grid(row=0, column=2, padx=10)
        
        # Ay-yıldız efekti için basit şekiller (Türk bayrağı sembolü olarak)
        self.ay_yildiz = tk.Canvas(self, width=100, height=100, bg="#E30A17", highlightthickness=0)
        self.ay_yildiz.place(x=20, y=20)
        # Ay (beyaz daire)
        self.ay_yildiz.create_oval(10, 10, 80, 80, fill="white", outline="white")
        # İç daire (kırmızı daire, ay efekti için)
        self.ay_yildiz.create_oval(25, 10, 95, 80, fill="#E30A17", outline="#E30A17")
        # Yıldız (basit beyaz)
        self.ay_yildiz.create_polygon(65, 30, 70, 45, 85, 45, 75, 55, 80, 70, 65, 60, 50, 70, 55, 55, 45, 45, 60, 45, fill="white")
        
        # Sonuç etiketi
        self.result_frame = tk.Frame(frame, bg='white')
        self.result_frame.pack(pady=10, fill=tk.X)
        
        self.result_label = tk.Label(self.result_frame, text="", font=("Arial", 12, "bold"), bg='white')
        self.result_label.pack(pady=5)
    
    def verify_tc(self):
        tc_no = self.tc_entry.get().strip()
        
        # TC kimlik numarası 11 haneli olmalı
        if not tc_no.isdigit() or len(tc_no) != 11:
            messagebox.showerror("Hata", "TC Kimlik Numarası 11 haneli rakamlardan oluşmalıdır.")
            return
            
        # İlk rakam 0 olamaz
        if tc_no[0] == '0':
            self.result_label.config(text="Geçersiz: İlk rakam 0 olamaz", fg='red')
            return
            
        # Son iki hane doğrulama - verilen algoritma ile
        num = tc_no[:9]
        haneler = [int(sayi) for sayi in num]
        
        hane10 = ((( haneler[0] + haneler[2] + haneler[4] + haneler[6] + haneler[8] )*7) - 
                  (haneler[1] + haneler[3] + haneler[5] + haneler[7])) % 10
                  
        hane11 = (haneler[0] + haneler[1] + haneler[2] + haneler[3] + haneler[4] + 
                 haneler[5] + haneler[6] + haneler[7] + haneler[8] + hane10) % 10
                 
        hesaplanan = str(hane10) + str(hane11)
        
        if tc_no[9:11] == hesaplanan:
            self.result_label.config(text="TC Kimlik Numarası Geçerlidir", fg='green')
        else:
            self.result_label.config(text="TC Kimlik Numarası Geçersizdir", fg='red')
    
    def clear_entry(self):
        self.tc_entry.delete(0, tk.END)
        self.result_label.config(text="")
    
    def generate_random_tc(self):
        # İlk 9 haneyi rastgele oluştur (ilk hane 0 olamaz)
        first_digit = random.randint(1, 9)
        other_digits = [random.randint(0, 9) for _ in range(8)]
        digits = [first_digit] + other_digits
        
        # 10. haneyi hesapla
        hane10 = (((digits[0] + digits[2] + digits[4] + digits[6] + digits[8]) * 7) - (digits[1] + digits[3] + digits[5] + digits[7]))
        hane10 = hane10 % 10
        
        # 11. haneyi hesapla
        hane11 = sum(digits) + hane10
        hane11 = hane11 % 10
        
        # TC kimlik numarasını oluştur
        tc_no = ''.join(map(str, digits)) + str(hane10) + str(hane11)
        
        # Entry alanına yerleştir
        self.tc_entry.delete(0, tk.END)
        self.tc_entry.insert(0, tc_no)
        self.result_label.config(text="Rastgele TC Kimlik No Üretildi", fg='blue')

if __name__ == "__main__":
    app = TCKimlikDogrulama()
    app.mainloop()
import sys
import io

#عشان يقبل الكلام العربي اللي بكتبه
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ENGLISH_BRAILLE = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕', 
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠖', 'w': '⠺', 'x': '⠭', 'y': '⠧', 'z': '⠵',
    ' ': ' '  
}


CAPITAL_SIGN = '⠠'

ARABIC_BRAILLE = {
    'أ': '⠁', 'ا': '⠁', 'آ': '⠜', 'إ': ' ⠡',
    'ب': '⠃', 'ت': '⠞', 'ث': '⠹', 'ج': '⠚', 'ح': '⠱', 'خ': '⠯', 
    'د': '⠙', 'ذ': '⠮', 'ر': '⠗', 'ز': '⠵', 'س': '⠎', 'ش': '⠩', 
    'ص': '⠯', 'ض': '⠫', 'ط': '⠾', 'ظ': '⠿', 'ع': '⠉', 'غ': '⠛', 
    'ف': '⠋', 'ق': '⠟', 'ك': '⠅', 'ل': '⠇', 'م': '⠍', 'ن': '⠝', 
    'ه': '⠓', 'و': '⠺', 'ي': '⠊', 'ى': '⠕', 'ة': '⠡', 'ئ': '⠽', 
    'ء': '⠄', 'ؤ': '⠳',
    ' ': ' ' 
}
DIGITS_BRAILLE = {
    '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙', '5': '⠑',
    '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊', '0': '⠚'
}

PUNCTUATION_BRAILLE = {
    '.': '⠲',   
    ',': '⠂',   
    '،': '⠐⠂', 
    '?': '⠦',   
    '؟': '⠦',  
    '!': '⠖',   
    ':': '⠒',  
    ';': '⠆',   
    '-': '⠤',   
    '(': '⠶',   
    ')': '⠶'    
}

# رموز التحكم الخاصة
CAPITAL_SIGN = '⠠'   # رمز الحرف الكبير للإنجليزي
NUMBER_SIGN = '⠼'    # مفتاح الأرقام



def translate_to_braille(text):
    braille_result = []
    in_number_mode = False  # مؤشر لمعرفة هل نحن داخل سلسلة أرقام أم لا
    
    for char in text:
        # أ) إذا كان الحرف رقماً
        if char.isdigit():
            if not in_number_mode:
                
                braille_result.append(NUMBER_SIGN)
                in_number_mode = True
            braille_result.append(DIGITS_BRAILLE[char])
            
        else:
            # ب) إذا كان الحرف ليس رقماً، نقوم بإلغاء وضع الأرقام
            in_number_mode = False
            
            # ج) التحقق من علامات الترقيم
            if char in PUNCTUATION_BRAILLE:
                braille_result.append(PUNCTUATION_BRAILLE[char])
                
            # د) إذا كان الحرف عربياً
            elif char in ARABIC_BRAILLE:
                braille_result.append(ARABIC_BRAILLE[char])
                
            # هـ) إذا كان إنجليزياً كابيتال
            elif char.isupper() and char.lower() in ENGLISH_BRAILLE:
                braille_result.append(CAPITAL_SIGN)
                braille_result.append(ENGLISH_BRAILLE[char.lower()])
                
            # و) إذا كان إنجليزياً سمول
            elif char in ENGLISH_BRAILLE:
                braille_result.append(ENGLISH_BRAILLE[char])
                
            # ز) أي رمز آخر غير معروف ينزل كما هو
            else:
                braille_result.append(char)
                
    return "".join(braille_result)

# 3. جزء التجربة (Testing Area)
if __name__ == "__main__":
    # نص للتجربة
    sample_text = "اهلا اهلا ,now i try my Code .......in english,والعربيو دي المحالولة رقم 123456 "
    
    print(f" test text: {sample_text}")
    translated = translate_to_braille(sample_text)
    print(f" in braile :  {translated}")
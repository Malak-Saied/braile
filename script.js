// 1. القواميس الأساسية لرموز برايل (Objects)
const ARABIC_BRAILLE = {
    'أ': '⠁', 'ا': '⠁', 'آ': '⠜', 'إ': 'Status: Active',
    'ب': '⠃', 'ت': '⠞', 'ث': '⠹', 'ج': '⠚', 'ح': '⠱', 'خ': '⠯', 
    'د': '⠙', 'ذ': '⠮', 'ر': '⠗', 'ز': '⠵', 'س': '⠎', 'ش': '⠩', 
    'ص': '⠯', 'ض': '⠫', 'ط': '⠾', 'ظ': '⠿', 'ع': '⠉', 'غ': '⠛', 
    'ف': '⠋', 'ق': '⠟', 'ك': '⠅', 'ل': '⠇', 'م': '⠍', 'ن': '⠝', 
    'ه': '⠓', 'و': '⠺', 'ي': '⠊', 'ى': '⠕', 'ة': '⠡', 'ئ': '⠽', 
    'ء': '⠄', 'ؤ': '⠳', ' ': ' '
};

const ENGLISH_BRAILLE = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕', 
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠖', 'w': '⠺', 'x': '⠭', 'y': '⠧', 'z': '⠵',
    ' ': ' '
};

const DIGITS_BRAILLE = {
    '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙', '5': '⠑',
    '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊', '0': '⠚'
};

const PUNCTUATION_BRAILLE = {
    '.': '⠲', ',': '⠂', '،': '⠐⠂', '?': '⠦', '؟': '⠦',
    '!': '⠖', ':': '⠒', ';': '⠆', '-': '⠤', '(': '⠶', ')': '⠶'
};

const CAPITAL_SIGN = '⠠';
const NUMBER_SIGN = '⠼';

// 2. دالة التحويل الذكية
function translateToBraille(text) {
    let brailleResult = [];
    let inNumberMode = false;

    for (let i = 0; i < text.length; i++) {
        let char = text[i];

        // أ) إذا كان رقماً
        if (char >= '0' && char <= '9') {
            if (!inNumberMode) {
                brailleResult.push(NUMBER_SIGN);
                inNumberMode = true;
            }
            brailleResult.push(DIGITS_BRAILLE[char]);
        } else {
            inNumberMode = false; // إلغاء وضع الأرقام عند ظهور أي حرف أو مسافة

            // ب) علامات الترقيم
            if (PUNCTUATION_BRAILLE[char]) {
                brailleResult.push(PUNCTUATION_BRAILLE[char]);
            }
            // ج) الحروف العربية
            else if (ARABIC_BRAILLE[char]) {
                brailleResult.push(ARABIC_BRAILLE[char]);
            }
            // د) الحروف الإنجليزية الكبيرة
            else if (char >= 'A' && char <= 'Z') {
                brailleResult.push(CAPITAL_SIGN);
                let lowerChar = char.toLowerCase();
                brailleResult.push(ENGLISH_BRAILLE[lowerChar] || char);
            }
            // هـ) الحروف الإنجليزية الصغيرة
            else if (ENGLISH_BRAILLE[char]) {
                brailleResult.push(ENGLISH_BRAILLE[char]);
            }
            // و) أي رمز آخر ينزل كما هو
            else {
                brailleResult.push(char);
            }
        }
    }
    return brailleResult.join("");
}

// 3. ربط عناصر الـ HTML بالترجمة الفورية
const inputArea = document.getElementById('userInput');
const resultDiv = document.getElementById('brailleResult');

// التأكد من وجود العناصر في الصفحة أولاً قبل ربط الأحداث لمنع الأخطاء
if (inputArea && resultDiv) {
    inputArea.addEventListener('input', function() {
        const text = inputArea.value;
        const brailleText = translateToBraille(text);
        resultDiv.textContent = brailleText;
    });
}
import pyttsx3, PyPDF2

## Designate path/name of file
file = filename
file_name = file.split(".", 1)[0]

## Initializing engine
pdfreader = PyPDF2.PdfReader(open(file, 'rb'))
speaker = pyttsx3.init()

## Setting voice
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)

## Compile whole text
text_compiler = ''

## Iterate through each page and combine to one long string
for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    text_compiler += clean_text
    print(clean_text)

## Save whole text extracted as mp3 file
speaker.save_to_file(text_compiler, f'{file_name}.mp3')
speaker.runAndWait()

speaker.stop()
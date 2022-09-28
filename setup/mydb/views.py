from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

import pandas as pd
from setup.constants import *
from .models import CharacterDetails

# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    return render(request, "home.html")



def read_excel(request):
    print('s')               
    try:
        if request.method == 'POST' and request.FILES['myfile']:

            EXCEL_FILENAME = "tmp.xlsx"
          
            myfile = request.FILES['myfile']        
            fs = FileSystemStorage()
            if fs.exists(EXCEL_FILENAME):
                fs.delete(EXCEL_FILENAME)
            filename = fs.save(EXCEL_FILENAME, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            print(excel_file) 
            df = pd.read_excel("."+excel_file)

            df = df.fillna('')

            print(df.columns)

            if spreadsheet_names[TABLE_COLUMN_NAME] in df.columns and spreadsheet_names[TABLE_COLUMN_TITLE] in df.columns:
                print("Reading spreadsheet...")

                for index, row in df.iterrows():
                    # find match

                    if not CharacterDetails.objects.filter(name=row[spreadsheet_names[TABLE_COLUMN_NAME]], title=row[spreadsheet_names[TABLE_COLUMN_TITLE]]).exists():
                        print(f"new entry for {row[spreadsheet_names[TABLE_COLUMN_NAME]]} from {row[spreadsheet_names[TABLE_COLUMN_TITLE]]}")

                        Character = CharacterDetails()

                        # for key, value in spreadsheet_names.items():
                        #     if spreadsheet_names[key] in df.columns:
                        #         #Character[key] = row[spreadsheet_names[key]]
                        #         setattr(Character, )
                        # print(Character.name)

                        #print(Character._meta.fields)


                        for field in Character._meta.fields:


                            (field_name, column_name) = field.get_attname_column()
                            if not field_name == "id":
                                if column_name in spreadsheet_names.keys() and spreadsheet_names[column_name] in df.columns:
                                    #print(field_name, row[spreadsheet_names[column_name]])

                                    if column_name == TABLE_COLUMN_CHARACTER_ID and row[spreadsheet_names[column_name]] == "":      
                                        setattr(Character, field_name, 0)
                                    else:
                                        setattr(Character, field_name, row[spreadsheet_names[column_name]])

                        Character.save()

                        

                    else:
                        print(f"skipping entry for {row[spreadsheet_names[TABLE_COLUMN_NAME]]} from {row[spreadsheet_names[TABLE_COLUMN_TITLE]]}")
            else:
                print("Wrong format!!")

            
 
            return render(request, 'importexcel.html', {
                'uploaded_file_url': uploaded_file_url
            })    
    except Exception as identifier:            
        print(identifier)
     
    return render(request, 'importexcel.html',{})
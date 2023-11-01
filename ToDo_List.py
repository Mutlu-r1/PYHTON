# task_todo_list = []

# def add_task(todo_list):
#     task = input("Yapılacak Görevi Girin: ")
#     todo_list.append(task)
#     print("Görev başarıyla eklendi!")

# def show_tasks(task_todo_list):  
#     print(task_todo_list)

# def delete_task(task_todo_list):
#     task = input("Silinecek Görevi yazın: ")
#     if task in task_todo_list:
#         task_todo_list.remove(task)
#         print("Görev başarıyla silindi!")
#     else:
#         print("Görev bulunamadı")


# while True:
#     print("To-Do List Uygulaması")
#     print("1. Görev Ekle")
#     print("2. Görevleri Göster")
#     print("3. Görevi sil")
#     print("4. ÇIKIŞ")
#     choice = input('seçiminiz: ')

#     if choice == "1":
#         add_task(task_todo_list)

#     elif choice == "2":
#         show_tasks(task_todo_list)

#     elif choice == "3":
#         delete_task(task_todo_list)

#     elif choice == "4":
#         print("Uygulamadan çıkılıyor...")
#         break
    
#     else:
#         print("Geçersiz seçim lütfen tekrar deneyiniz")
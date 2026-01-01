import tkinter as tk
from views import AboutFrame,DeleteFrame,ChangeFrame,InsertFrame,SearchFrame

class MianPage:
    def __init__(self,master:tk.Tk):
        self.root = master 
        self.root.title('学生信息管理系统 v0.0.1')
        self.root.geometry('600x400')
        # 在创建对象时自动初始化并显示界面
        self.create_page()

    def create_page(self):
        self.insert_frame = InsertFrame(self.root)
        self.search_frame = SearchFrame(self.root)
        self.delete_frame = DeleteFrame(self.root)
        self.change_frame = ChangeFrame(self.root)
        self.about_frame = AboutFrame(self.root)

        self.menubar = tk.Menu(self.root)
        self.menubar.add_command(label='录入', command=self.show_insert)
        self.menubar.add_command(label='查询', command=self.show_search)
        self.menubar.add_command(label='删除', command=self.show_delete)
        self.menubar.add_command(label='修改', command=self.show_change)
        self.menubar.add_command(label='关于', command=self.show_about)
        self.root['menu'] = self.menubar
    
    def hide_all_frames(self):
        """隐藏所有页面"""
        self.insert_frame.pack_forget()
        self.search_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.change_frame.pack_forget()
        self.about_frame.pack_forget()
    
    def show_insert(self):
        self.hide_all_frames()  
        self.insert_frame.pack()

    def show_search(self):
        self.hide_all_frames()  
        self.search_frame.pack()

    def show_delete(self):
        self.hide_all_frames()  
        self.delete_frame.pack()

    def show_change(self):
        self.hide_all_frames()  
        self.change_frame.pack()
                
    def show_about(self):
        self.hide_all_frames()  
        self.about_frame.pack()
        
if __name__ == '__main__':
    root = tk.Tk()
    MianPage(master = root)
    root.mainloop()
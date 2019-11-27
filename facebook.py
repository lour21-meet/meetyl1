users =[]
posts = []
class User():
	def __init__(self,name,email,password,friends_list,posts):
		self.name = name
		self.email = email
		self.password = password
		self.friends_list = friends_list
		self.posts = posts
		users.append(self)

	def add_friends(self,email):
		self.friends_list.append(email)
		print(self.name + ' has added ' + email + ' as a friend.')
	def remove_friends(self,email):
		self.friends_list.remove(email)
		print(self.name + ' has removed ' + email + ' as a friend')
	def new_post(self,text,location,tags,comments):
		post1 = Post(self.name, text,location,tags,comments)
		self.posts.append(post1)
		print(self.name + ' has posted:' +  text)
		posts.append(post)
	def get_userInfo(self):
		print('Name: ' +  self.name + ' Email: ' + self.email + ' Password: ' + self.password + ' Friends: ' + str(self.friends_list) + " Posts: " + str(self.posts))
class Post():
	def __init__(self,name,location,tags,caption,comments):
		self.name = name
		self.location= location
		self.tags= tags
		self.caption= caption
		self.comments=comments
	def tagppl(self,email):
		self.tags.append(name)
		print(self.name + ' is with ' + email " in " + self.location)
	def addcomments(self,text,email):
		self.comments.apend(text)
		print(email + ' commented on '+ self.name + ":" + text " 's post")



user1 = User('Albert','Albert12@gmail.com','iamalbert', [], [])
user2 = User('Loai','Loai13@gmail.com','mynameisl',[],[])
user1.add_friends('ahmad@gmail.com')
user1.add_friends('Loai13@gmail.com')
user1.post('surviving')
user1.get_userInfo()
user1.remove_friends('ahmad@gmail.com')
user1.post('living','earth','Loai','have fun')

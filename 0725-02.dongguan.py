#coding=utf-8

class road:
	def __init__(self):
		self.juli=100
		self.shijian=0
	def run(self,shijian):
		self.shijian=shijian
		if self.shijian>=60:
			shengyu=self.juli-self.shijian*0.5
			print('剩余距离是%d KM'%shengyu)
			if shengyu<=20:
				print('很快就到了')
			else:
				print('狂踩油门！！！')
		else:
			print('开飞机呢？')

print('马上开路！！！！')
dongguan=road()
print('开路20分钟！！！')
dongguan.run(20)#开飞机呢？	
print('开路60分钟！！')
dongguan.run(60)#距离70,狂踩油门
print('开路120分钟')
dongguan.run(120)#距离40,狂踩油门
print('开路160分钟')
dongguan.run(160)

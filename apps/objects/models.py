import random
from django.db import models

#generic snake stuff
class Base_Snake(models.Model):
	# def __init__():
	# 	pass

	alive = models.BooleanField(default=True)
	
class PlayerSnake(Base_Snake):
	def __init__(self, *args, **kwargs):
		super(PlayerSnake, self).__init__(*args, **kwargs)
		self.body = [(25,25)]
		self.dir = (1, 0)

class EnemySnake(Base_Snake):
	def __init__(self, x, y, *args, **kwargs):
		super(EnemySnake, self).__init__(*args, **kwargs)
		self.body = [(x,y)]
		self.dir = (1, 0)


class SnakeFood(models.Model):
	def __init__(self, x, y):
		self.position = (x,y)



 #	  user = models.OneToOneField(User, related_name='settings')
 #    message_notifications_enabled = models.BooleanField(default=True)
 #    transfer_notifications_enabled = models.BooleanField(default=True)
 #    task_notifications_enabled = models.BooleanField(default=True)
 #    bookkeeping_notifications_enabled = models.BooleanField(default=True)
 #    reward_notifications_enabled = models.BooleanField(default=True)
 #    shopping_notifications_enabled = models.BooleanField(default=True)

 #    balance_notifications_enabled = models.BooleanField(default=True)
 #    balance_notification_threshold = models.FloatField(default=DEFAULT_BALANCE_NOTIFICATION_THRESHOLD)
 #    #to avoid repeat sending of threshold notificaiton, set this to true until it dips below the threshold again.
 #    balance_notification_sent = models.BooleanField(default=False)
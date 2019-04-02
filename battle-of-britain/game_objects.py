'''
This file will contain all the game objects (classes). To make main file easer to read.
'''
# pylint: disable=import-error
import math
import random
import pygame
import settings

class Ship(pygame.sprite.Sprite):
    '''
    This is the class of the ship. It will
    handle movement, decteding weather it was shhot. and updating.
    '''
    def __init__(self, ship_x, ship_y, image,):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = ship_x
        self.rect.y = ship_y

        self.heath = settings.SHIP_MAX_HEALTH
        self.speed = 3

    def move_left(self):
        '''
        moves space ship left
        '''
        self.rect.x -= self.speed

    def move_right(self):
        '''
        moves space ship right
        '''
        self.rect.x += self.speed

    def shoot(self):
        '''
        this will start the process of a laser being shot from the ship.
        '''

        laser = Laser(settings.LASER_IMG)
        laser.rect.centerx = self.rect.centerx
        laser.rect.centery = self.rect.top
        settings.LASERS.add(laser)


    def update(self):
        '''
        this will up date the ship.
            See if it has hit walls
        '''

        if self.rect.left < 0:
            self.rect.left = 0

        elif self.rect.right > settings.WIDTH:
            self.rect.right = settings.WIDTH

        hit_list = pygame.sprite.spritecollide(self, settings.BOMBS,
                                               True, pygame.sprite.collide_mask)
        if hit_list:
            # print('Outch')
            self.heath -= 10


        hit_list = pygame.sprite.spritecollide(self, settings.FIREBALL,
                                               True, pygame.sprite.collide_mask)

        if hit_list:
            self.heath -= 20

        if self.heath <= 0:
            self.kill()


class Laser(pygame.sprite.Sprite):
    '''
    This class will hold all the lasers shot. And will move and kill them.
    '''
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()

        self.speed = 5

    def update(self):
        '''
        Move the lasers up the screen and will delete them when appoiot
        '''
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()


class Mob(pygame.sprite.Sprite):
    '''
    This class will house all the enemies and update them.
    '''
    def __init__(self, mob_x, mob_y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = mob_x
        self.rect.y = mob_y


    def drop_bomb(self):
        '''
        This is acctually shoot the enemy lasers
        '''
        if not self.rect.bottom < 0:
            bomb = Bomb(settings.BOMB_IMG)
            bomb.rect.centerx = self.rect.centerx
            bomb.rect.centery = self.rect.bottom
            settings.BOMBS.add(bomb)



    def after_death(self):
        '''
        After the enemy plane is shot this is will do what it needs to do after that.
        '''
        fireball = FireBall(settings.FIREBALL_IMG)
        fireball.rect.centerx = self.rect.centerx
        fireball.rect.centery = self.rect.bottom
        settings.FIREBALL.add(fireball)

    def update(self):
        '''
        This will check to see if the mobs have been hit.
        '''
        hit_list = None
        if not self.rect.bottom < 0:
            hit_list = pygame.sprite.spritecollide(self, settings.LASERS,
                                                   True, pygame.sprite.collide_mask)

        for bullet in settings.BULLETS:
            if bullet.reverse:
                hit_list_2 = pygame.sprite.spritecollide(self, settings.BULLETS,
                                                         True, pygame.sprite.collide_mask)
                if hit_list_2:
                    settings.KILLS_CONFIRMED += 1
                    self.kill()
        if hit_list:
            settings.KILLS_CONFIRMED += 1
            self.after_death()
            self.kill()
            settings.EXPLOSION_SOUND.play()


class Bomb(pygame.sprite.Sprite):
    '''
    This class will hold all the bombs shot. And will move and kill them.
    '''
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()

        self.speed = 3

    def update(self):
        '''
        Move the lasers up the screen and will delete them when appoiot.
        '''
        self.rect.y += self.speed
        if self.rect.top > settings.HEIGHT:
            self.kill()


class FireBall(pygame.sprite.Sprite):
    '''
    This class will hold all the bombs shot. And will move and kill them.
    '''
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()

        self.speed = 6

    def update(self):
        '''
        Move the lasers up the screen and will delete them when appoiot.
        '''
        self.rect.y += self.speed
        if self.rect.top > settings.HEIGHT:
            self.kill()


class Fleet():
    '''
    This is a class of the mobs where it will process their movement.
    '''
    def __init__(self, mobes):
        self.mobs = mobes
        self.speed = 3
        self.moving_right = True
        self.drop_speed = 5
        self.bomb_rate = 3

    def move(self):
        '''
        This function will move the fleet.
        '''
        hits_edge = False
        on_screen = []

        for _m in settings.MOBS:

            if not _m.rect.bottom <= 0:
                on_screen.append(_m)

                if self.moving_right:
                    _m.rect.x += self.speed

                    if _m.rect.right >= settings.WIDTH and _m.rect.bottom >= 0:
                        hits_edge = True

                else:
                    _m.rect.x -= self.speed
                    if _m.rect.left <= 0:
                        hits_edge = True
            else:
                pass

        if hits_edge:
            self.reverse()
            self.move_down()
        elif not on_screen:
            self.move_down()

    def reverse(self):
        '''
        IDK WHY THIS HAS TO BE A FUNCTION
        '''
        self.moving_right = not self.moving_right

    def move_down(self):
        '''
        This runs through all the mobs, then moves them down.
        '''
        for mob in self.mobs:
            mob.rect.y += self.drop_speed

    def speed_up(self):
        '''
        make the ships move faster.
        '''
        if settings.PLAYING_FRAME % 600 == 0: # every 10 secounds
            self.speed += 1
        if settings.PLAYING_FRAME % 1800 == 0: # every 30 secounds
            self.bomb_rate -= 1

    def choose_bomber(self):
        '''
        This will randoly choose which bomber will shoot,
        And how often it will shoot.
        '''
        rand = random.randrange(self.bomb_rate)
        mob_list = settings.MOBS.sprites()

        if mob_list and rand == 0:
            bomber = random.choice(mob_list)
            bomber.drop_bomb()

    def update(self):
        '''
        updates the fleet
        '''
        if settings.STAGE == settings.PLAYING:
            self.move()
            self.choose_bomber()
            self.speed_up()
            # print(self.speed)

        elif settings.STAGE == settings.LOST:
            self.move_down()

        else:
            pass

class Sentry(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.lives = 10

    def drop_bullet(self):
        bullet = Bullet(settings.BOMB_IMG)
        bullet.rect.centerx = self.rect.centerx
        bullet.rect.centery = self.rect.bottom
        settings.BULLETS.add(bullet)

        settings.SHOOT_SOUND.play()

    def update(self):
        hit_list = pygame.sprite.spritecollide(self, settings.BOMBS, True, pygame.sprite.collide_mask)
        temp = random.randrange(0, 200)
        if len(hit_list) > 0:
            self.lives -= 1
            if self.lives == 0:
                settings.KILLS_CONFIRMED += 1
                self.kill()
        if temp == 42:
            self.drop_bullet()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.speed = 5
        self.theta = None
        self.dis_dis = None
        self.perception_rad = 75.0
        self.velocity = []
        self.reverse = False
    def shoot(self):
        settings.SHOOT_SOUND.play()

    def find_theta(self):

        dis_x = settings.SHIP.rect.centerx - self.rect.centerx
        dis_y = settings.SHIP.rect.centery - self.rect.centery
        self.dis_dis = math.sqrt((dis_x**2 + dis_y**2))

        if self.dis_dis == 0:
            # Mark Gyomory
            self.kill()
        else:
            self.theta = math.asin(dis_x/self.dis_dis)

        self.find_velocity()

    def find_velocity(self):
        vx = math.sin(self.theta) * self.speed
        # Mark Gyomory
        vy = math.cos(self.theta) * self.speed
        self.velocity = [vx, vy]


    def update(self):
        self.find_theta()
        if self.dis_dis > self.perception_rad and not self.reverse :
            pass
        else:
            self.reverse = True
            self.velocity[0] *= -1
            self.velocity[1] *= -1

        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


        self.image = pygame.transform.rotate(settings.BOMB_IMG, math.degrees(self.theta))

        if self.rect.bottom > settings.HEIGHT:
            self.kill()


class Fleet2():
    def __init__(self, mobs):
        self.mobs = mobs
        self.speed = 5
        self.moving_right = True
        self.move_down_num = 7
        self.bombing_rate = 20 #Lower is faster

        self.make_sentrys()

        self.wave_num = 1

    def move(self):
        hits_edge = False

        for m in settings.MOBS:
            if self.moving_right:
                m.rect.x += self.speed

                if m.rect.right >= settings.WIDTH:
                    hits_edge = True

            else:
                m.rect.x -= self.speed

                if m.rect.left <= 0:
                    hits_edge = True
        if hits_edge:
            self.reverse()
            self.move_down()

    def reverse(self):
        self.moving_right = not self.moving_right

    def move_down(self):
        for m in settings.MOBS:
            m.rect.y += self.move_down_num

    def choose_bomber(self):
        rand = random.randrange(self.bombing_rate)
        mob_list = settings.MOBS.sprites()

        if len(mob_list) > 0 and rand == 0:
            bomber = random.choice(mob_list)
            bomber.drop_bomb()


    def make_sentrys(self):
        settings.SENTRYS.add(Sentry(50, settings.HEIGHT * (4/10), settings.FLACK_TOWER_IMG))
        settings.SENTRYS.add(Sentry(settings.WIDTH - 100, settings.HEIGHT * (4/10), settings.FLACK_TOWER_IMG))


    def kill(self):
        for a in settings.MOBS():
            self.kill()

    def update(self):
        if len(settings.MOBS) == 0:
            self.wave_num += 1
            self.bombing_rate -= 3
            if self.bombing_rate <= 0:
                self.bombing_rate = 1

            self.move_down_num += 3
            if self.move_down_num <= 0:
                self.move_down_num = 1

            self.make_sentrys()

        for m in settings.MOBS:
            if m.rect.bottom >= settings.HEIGHT - 150:
                settings.PLAYER.heath = 0

        if settings.PLAYER.heath <= 0:
            self.mobs.empty()

        self.move()
        self.choose_bomber()

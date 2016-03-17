#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

print "Iniciando o Código"

print "Configurando o Esquema de numeração dos ports"
GPIO.setmode(GPIO.BCM)

print "Configurando os Ports como saída"
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

print "Criando os objetos Led"
led1	= GPIO.PWM(17, 100) #Direita Para Frente
led2	= GPIO.PWM(22, 100) #Direita Para Tras
led3	= GPIO.PWM(23, 100) #Esquerda Para Frente
led4	= GPIO.PWM(27, 100) #Esquerda Para Tras 

print "Acendendo os Leds"
led1.start(100) #Duty Cycle de 100%
time.sleep(1)
led2.start(100) #Duty Cycle de 100%
time.sleep(1)
led3.start(100) #Duty Cycle de 100%
time.sleep(1)
led4.start(100) #Duty Cycle de 100%

print "Waiting....."
time.sleep(10)

print "Apagando os leds"
led4.stop()
time.sleep(1)
led3.stop()
time.sleep(1)
led2.stop()
time.sleep(1)
led1.stop()

print "Limpando as configurações dos ports"
GPIO.cleanup()

print "Fim da execução do programa"
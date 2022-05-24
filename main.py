#TODO There is no same step

import pygame, sys, time, os, copy
from pygame.locals import *
from Settings import *
import random
import webbrowser

pygame.init()
mainclock = pygame.time.Clock()
WINDOWSURFACE = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption(TITLE)
pygame.font.init()
backgroundColor = GREY
textColor = WHITE
secondaryColor = PINK
oldSecondaryColor = PINK
boxColor = RED
oldBoxColor = GREY
smallFont = pygame.font.SysFont("Times New Roman", 15)
font = pygame.font.SysFont("Times New Roman", 25, bold = True)
bigFont = pygame.font.SysFont("Times New Roman", 49, bold = True)
superFont = pygame.font.SysFont("Times New Roman", 400)
AnswerFont = pygame.font.SysFont("Times New Roman", 20)
HomeScreenRectangle = pygame.Rect(WINDOWWIDTH / 15, WINDOWHEIGHT / 15, WINDOWWIDTH - 2 * WINDOWWIDTH / 15, WINDOWHEIGHT - 2 * WINDOWHEIGHT / 15)
VisualScreenButton = pygame.Rect(WINDOWWIDTH / 3, WINDOWHEIGHT / 10, WINDOWWIDTH - 2 * WINDOWWIDTH / 3, WINDOWHEIGHT / 15)
AlgorithmScreenButton = pygame.Rect(WINDOWWIDTH / 3, 2*(WINDOWHEIGHT / 10) + (WINDOWHEIGHT / 15), WINDOWWIDTH - 2 * WINDOWWIDTH / 3, WINDOWHEIGHT / 15)
VisualRepresentationScreenButton = pygame.Rect(WINDOWWIDTH / 15, WINDOWHEIGHT / 15, WINDOWWIDTH - 2 * WINDOWWIDTH / 15, 2*WINDOWHEIGHT / 15)
AlgorithmRepresentationScreenButton = pygame.Rect(WINDOWWIDTH / 15, WINDOWHEIGHT / 15, WINDOWWIDTH - 2 * WINDOWWIDTH / 15, 2*WINDOWHEIGHT / 15)
StepByStepScreenButton = pygame.Rect(WINDOWWIDTH / 3, WINDOWHEIGHT / 3, WINDOWWIDTH - 2 * WINDOWWIDTH / 3, WINDOWHEIGHT / 15)
AutomaticScreenButton = pygame.Rect(WINDOWWIDTH / 3, 2*(WINDOWHEIGHT / 5) + (WINDOWHEIGHT / 15), WINDOWWIDTH - 2 * WINDOWWIDTH / 3, WINDOWHEIGHT / 15)
BackButton = pygame.Rect(WINDOWWIDTH / 10, WINDOWHEIGHT - (WINDOWHEIGHT / 6), WINDOWWIDTH / 8, WINDOWHEIGHT / 10)
OneButton = pygame.Rect(WINDOWWIDTH / 3, WINDOWHEIGHT / 3, WINDOWWIDTH / 15, WINDOWHEIGHT / 15)
TwoButton = pygame.Rect(7*WINDOWWIDTH / 15, WINDOWHEIGHT / 3, WINDOWWIDTH / 15, WINDOWHEIGHT / 15)
ThreeButton = pygame.Rect(9*WINDOWWIDTH / 15, WINDOWHEIGHT / 3, WINDOWWIDTH / 15, WINDOWHEIGHT / 15)
FourButton = pygame.Rect(WINDOWWIDTH / 3, 7*WINDOWHEIGHT / 15, WINDOWWIDTH / 15, WINDOWHEIGHT / 15)
FiveButton = pygame.Rect(7*WINDOWWIDTH / 15, 7*WINDOWHEIGHT / 15, WINDOWWIDTH / 15, WINDOWHEIGHT / 15)
SixButton = pygame.Rect(9*WINDOWWIDTH / 15, 7*WINDOWHEIGHT / 15, WINDOWWIDTH / 15, WINDOWHEIGHT / 15)
SevenButton = pygame.Rect(WINDOWWIDTH / 3, 9*WINDOWHEIGHT / 15, WINDOWWIDTH / 15, WINDOWHEIGHT / 15)
EightButton = pygame.Rect(7*WINDOWWIDTH / 15, 9*WINDOWHEIGHT / 15, WINDOWWIDTH / 15, WINDOWHEIGHT / 15)
NineButton = pygame.Rect(9*WINDOWWIDTH / 15, 9*WINDOWHEIGHT / 15, WINDOWWIDTH / 15, WINDOWHEIGHT / 15)
FrontToBackScreenButton = pygame.Rect(2*WINDOWWIDTH / 6, WINDOWHEIGHT / 10, WINDOWWIDTH / 3, WINDOWHEIGHT / 15)
OnRodButton = pygame.Rect(1*WINDOWWIDTH / 15, 3*WINDOWHEIGHT / 10, WINDOWWIDTH / 7, WINDOWHEIGHT / 15)
OffRodButton = pygame.Rect(1*WINDOWWIDTH / 15, 4.5*WINDOWHEIGHT / 10, WINDOWWIDTH / 7, WINDOWHEIGHT / 15)
NextStepButton = pygame.Rect(WINDOWWIDTH - 3*(WINDOWWIDTH / 10), WINDOWHEIGHT - 3*(WINDOWHEIGHT / 7), WINDOWWIDTH / 7, WINDOWHEIGHT / 10)
NumberChosen = 0
firstRingNumber = pygame.Rect(3 * WINDOWWIDTH / 15, 3 * WINDOWHEIGHT / 10 - 10, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
secondRingNumber = pygame.Rect(4 * WINDOWWIDTH / 15, 3 * WINDOWHEIGHT / 10 - 10, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
thirdRingNumber = pygame.Rect(5 * WINDOWWIDTH / 15, 3 * WINDOWHEIGHT / 10 - 10, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
fourthRingNumber = pygame.Rect(6 * WINDOWWIDTH / 15, 3 * WINDOWHEIGHT / 10 - 10, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
fifthRingNumber = pygame.Rect(7 * WINDOWWIDTH / 15, 3 * WINDOWHEIGHT / 10 - 10, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
sixthRingNumber = pygame.Rect(8 * WINDOWWIDTH / 15, 3 * WINDOWHEIGHT / 10 - 10, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
seventhRingNumber = pygame.Rect(9 * WINDOWWIDTH / 15, 3 * WINDOWHEIGHT / 10 - 10, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
eighthRingNumber = pygame.Rect(10 * WINDOWWIDTH / 15, 3 * WINDOWHEIGHT / 10 - 10, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
ninthRingNumber = pygame.Rect(11 * WINDOWWIDTH / 15, 3 * WINDOWHEIGHT / 10 - 10, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
oneExplanation = pygame.Rect(WINDOWWIDTH / 6, 2*WINDOWHEIGHT / 10, WINDOWWIDTH / 3, WINDOWHEIGHT / 15)
zeroExplanation = pygame.Rect(3*WINDOWWIDTH / 6, 2*WINDOWHEIGHT / 10, WINDOWWIDTH / 3, WINDOWHEIGHT / 15)
setNumberExplanation = pygame.Rect(WINDOWWIDTH / 15, WINDOWHEIGHT / 15, WINDOWWIDTH - 2 * WINDOWWIDTH / 15, WINDOWHEIGHT / 15)
setNumberExplanationEnter = pygame.Rect(WINDOWWIDTH / 15, (WINDOWHEIGHT/15) + (WINDOWHEIGHT / 15), WINDOWWIDTH - 2 * WINDOWWIDTH / 15, WINDOWHEIGHT / 15)
visualAlgorithmExplanation = pygame.Rect(WINDOWWIDTH / 4, WINDOWHEIGHT / 2, WINDOWWIDTH / 2, WINDOWHEIGHT / 15)
visualAlgorithmExplanation2 = pygame.Rect(WINDOWWIDTH / 4, (WINDOWHEIGHT / 2)+WINDOWHEIGHT / 20, WINDOWWIDTH / 2, WINDOWHEIGHT / 20)
visualAlgorithmExplanation3 = pygame.Rect(WINDOWWIDTH / 4, (WINDOWHEIGHT / 2)+2*WINDOWHEIGHT / 20, WINDOWWIDTH / 2, WINDOWHEIGHT / 20)
hideText = pygame.Rect(0, 3*WINDOWHEIGHT / 15, WINDOWWIDTH, WINDOWHEIGHT)
nameCredit = pygame.Rect(0, WINDOWHEIGHT-50, WINDOWWIDTH / 4, 25)
courseCredit = pygame.Rect(0, WINDOWHEIGHT-25, WINDOWWIDTH / 4, 25)
onOffExplanation = pygame.Rect(WINDOWWIDTH / 3, WINDOWHEIGHT - 3*(WINDOWHEIGHT / 7), WINDOWWIDTH / 3, WINDOWHEIGHT / 10)
settingButton = pygame.Rect(8*WINDOWWIDTH / 10, WINDOWHEIGHT - (WINDOWHEIGHT / 6), WINDOWWIDTH / 8, WINDOWHEIGHT / 10)
whiteButton = pygame.Rect(2*WINDOWWIDTH/9, 2*WINDOWHEIGHT/9, WINDOWWIDTH / 7, WINDOWHEIGHT/9)
blackButton = pygame.Rect(4*WINDOWWIDTH/9, 2*WINDOWHEIGHT/9, WINDOWWIDTH / 7, WINDOWHEIGHT/9)
greyButton = pygame.Rect(6*WINDOWWIDTH/9, 2*WINDOWHEIGHT/9, WINDOWWIDTH / 7, WINDOWHEIGHT/9)
redButton = pygame.Rect(2*WINDOWWIDTH/9, 4*WINDOWHEIGHT/9, WINDOWWIDTH / 7, WINDOWHEIGHT/9)
greenButton = pygame.Rect(4*WINDOWWIDTH/9, 4*WINDOWHEIGHT/9, WINDOWWIDTH / 7, WINDOWHEIGHT/9)
blueButton = pygame.Rect(6*WINDOWWIDTH/9, 4*WINDOWHEIGHT/9, WINDOWWIDTH / 7, WINDOWHEIGHT/9)
pinkButton = pygame.Rect(2*WINDOWWIDTH/9, 6*WINDOWHEIGHT/9, WINDOWWIDTH / 7, WINDOWHEIGHT/9)
goldButton = pygame.Rect(4*WINDOWWIDTH/9, 6*WINDOWHEIGHT/9, WINDOWWIDTH / 7, WINDOWHEIGHT/9)
lightBlueButton = pygame.Rect(6*WINDOWWIDTH/9, 6*WINDOWHEIGHT/9, WINDOWWIDTH / 7, WINDOWHEIGHT/9)
backgroundColorTab = pygame.Rect(WINDOWWIDTH/9, WINDOWHEIGHT/15, WINDOWWIDTH / 6, WINDOWHEIGHT/15)
textColorTab = pygame.Rect((WINDOWWIDTH/9) + (WINDOWWIDTH / 6) + (800/27), WINDOWHEIGHT/15, WINDOWWIDTH / 6, WINDOWHEIGHT/15)
boxColorTab = pygame.Rect((WINDOWWIDTH/9) + 2*(WINDOWWIDTH / 6) + 2*(800/27), WINDOWHEIGHT/15, WINDOWWIDTH / 6, WINDOWHEIGHT/15)
secondaryBoxColorTab = pygame.Rect((WINDOWWIDTH/9) + 3*(WINDOWWIDTH / 6) + 3*(800/27), WINDOWHEIGHT/15, WINDOWWIDTH / 6, WINDOWHEIGHT/15)


def DrawHearts(Player, Surface):
    global FullHeartImage, EmptyHeartImage
    position = (550, 70)
    ScaledFullHeartImage = pygame.transform.scale(FullHeartImage, (30, 30))
    ScaledEmptyHeartImage = pygame.transform.scale(EmptyHeartImage, (30, 30))
    currentHealth = Player.health
    healthLost = Player.maxhealth - Player.health
    while healthLost > 0:
        Surface.blit(ScaledEmptyHeartImage, position)
        position = (position[0] - 30, position[1])
        healthLost = healthLost - 1
    while currentHealth > 0:
        Surface.blit(ScaledFullHeartImage, position)
        position = (position[0] - 30, position[1])
        currentHealth = currentHealth - 1

def RefreshScreen():
    pygame.display.update()  # Once per while loop, refreshes the screen
    mainclock.tick(FPS)  # At the end of every while loop

def quitPygame():
    pygame.quit()
    sys.exit()

def checkTermination(event):
    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
        quitPygame()

def IntroductionScreen():
    global WINDOWSURFACE, NumberChosen
    Color1 = Color2 = Color3 = Color4 = Color5 = Color6 = Color7 = Color8 = Color9 = Color10 = boxColor
    DefaultColor = boxColor
    NewColor = secondaryColor
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    color = pygame.Color('dodgerblue2')
    text = ''


    while True:

        pygame.draw.rect(WINDOWSURFACE, Color1, setNumberExplanation)
        VisualChoiceText = font.render("Type a number between 1-9 inclusive", True, textColor, Color1)
        VisualTextRectangle = VisualChoiceText.get_rect()
        VisualTextRectangle.center = (setNumberExplanation.center)
        VisualChoiceTextRect = VisualChoiceText.get_rect(center=setNumberExplanation.center)
        WINDOWSURFACE.blit(VisualChoiceText, VisualChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, Color1, setNumberExplanationEnter)
        VisualChoiceText2 = font.render("Press enter once you type a number", True, textColor, Color1)
        VisualTextRectangle2 = VisualChoiceText2.get_rect()
        VisualTextRectangle2.center = (setNumberExplanationEnter.center)
        VisualChoiceTextRect2 = VisualChoiceText2.get_rect(center=setNumberExplanationEnter.center)
        WINDOWSURFACE.blit(VisualChoiceText2, VisualChoiceTextRect2)

        pygame.draw.rect(WINDOWSURFACE, BLACK, hideText)
        VisualChoiceText = font.render("", True, BLACK, BLACK)
        VisualTextRectangle = VisualChoiceText.get_rect()
        VisualTextRectangle.center = (hideText.center)
        VisualChoiceTextRect = VisualChoiceText.get_rect(center=hideText.center)
        WINDOWSURFACE.blit(VisualChoiceText, VisualChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, Color1, nameCredit)
        nameCreditChoiceText = smallFont.render("by Taiki Nagao", True, textColor, Color1)
        nameCreditTextRectangle = nameCreditChoiceText.get_rect()
        nameCreditTextRectangle.center = (nameCredit.center)
        nameCreditChoiceTextRect = nameCreditChoiceText.get_rect(center=nameCredit.center)
        WINDOWSURFACE.blit(nameCreditChoiceText, nameCreditChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, Color1, courseCredit)
        courseCreditChoiceText = smallFont.render("MVC and Linear Algebra", True, textColor, Color1)
        courseCreditTextRectangle = courseCreditChoiceText.get_rect()
        courseCreditTextRectangle.center = (courseCredit.center)
        courseCreditChoiceTextRect = courseCreditChoiceText.get_rect(center=courseCredit.center)
        WINDOWSURFACE.blit(courseCreditChoiceText, courseCreditChoiceTextRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if text == str(1):
                        NumberChosen = 1
                        StartScreen()
                    if text == str(2):
                        NumberChosen = 2
                        StartScreen()
                    if text == str(3):
                        NumberChosen = 3
                        StartScreen()
                    if text == str(4):
                        NumberChosen = 4
                        StartScreen()
                    if text == str(5):
                        NumberChosen = 5
                        StartScreen()
                    if text == str(6):
                        NumberChosen = 6
                        StartScreen()
                    if text == str(7):
                        NumberChosen = 7
                        StartScreen()
                    if text == str(8):
                        NumberChosen = 8
                        StartScreen()
                    if text == str(9):
                        NumberChosen = 9
                        StartScreen()
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
        txt_surface = superFont.render(text, True, color)
        WINDOWSURFACE.blit(txt_surface, (300, 200))

        pygame.display.flip()
        clock.tick(30)
        RefreshScreen()


def StartScreen():
    global WINDOWSURFACE, backgroundColor, textColor, secondaryColor, oldBoxColor
    Color = Color1 = Color2 = Color3 = boxColor
    DefaultColor = boxColor
    NewColor = secondaryColor
    showExplanation = 0
    while True:
        if Color1 == oldBoxColor or Color2 == oldBoxColor or Color3 == oldBoxColor:
            Color1 = Color2 = Color3 = boxColor
        WINDOWSURFACE.fill(BLACK)
        pygame.draw.rect(WINDOWSURFACE, backgroundColor, HomeScreenRectangle)

        pygame.draw.rect(WINDOWSURFACE, Color1, VisualScreenButton)
        VisualChoiceText = font.render("Visual", True, textColor, Color1)
        VisualTextRectangle = VisualChoiceText.get_rect()
        VisualTextRectangle.center = (VisualScreenButton.center)
        VisualChoiceTextRect = VisualChoiceText.get_rect(center=VisualScreenButton.center)
        WINDOWSURFACE.blit(VisualChoiceText, VisualChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, Color2, AlgorithmScreenButton)
        AlgorithmChoiceText = font.render("Algorithm", True, textColor, Color2)
        AlgorithmTextRectangle = AlgorithmChoiceText.get_rect()
        AlgorithmTextRectangle.center = (AlgorithmScreenButton.center)
        AlgorithmChoiceTextRect = AlgorithmChoiceText.get_rect(center=AlgorithmScreenButton.center)
        WINDOWSURFACE.blit(AlgorithmChoiceText, AlgorithmChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, boxColor, nameCredit)
        nameCreditChoiceText = smallFont.render("by Taiki Nagao", True, textColor, boxColor)
        nameCreditTextRectangle = nameCreditChoiceText.get_rect()
        nameCreditTextRectangle.center = (nameCredit.center)
        nameCreditChoiceTextRect = nameCreditChoiceText.get_rect(center=nameCredit.center)
        WINDOWSURFACE.blit(nameCreditChoiceText, nameCreditChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, boxColor, courseCredit)
        courseCreditChoiceText = smallFont.render("MVC and Linear Algebra", True, textColor, boxColor)
        courseCreditTextRectangle = courseCreditChoiceText.get_rect()
        courseCreditTextRectangle.center = (courseCredit.center)
        courseCreditChoiceTextRect = courseCreditChoiceText.get_rect(center=courseCredit.center)
        WINDOWSURFACE.blit(courseCreditChoiceText, courseCreditChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, Color3, settingButton)
        settingButtonChoiceText = font.render("Setting", True, textColor, Color3)
        settingButtonTextRectangle = settingButtonChoiceText.get_rect()
        settingButtonTextRectangle.center = (settingButton.center)
        settingButtonChoiceTextRect = settingButtonChoiceText.get_rect(center=settingButton.center)
        WINDOWSURFACE.blit(settingButtonChoiceText, settingButtonChoiceTextRect)

        if showExplanation == 1:
            pygame.draw.rect(WINDOWSURFACE, boxColor, visualAlgorithmExplanation)
            visualAlgorithmChoiceText = font.render("Model for the Chinese",
                                                    True, textColor, boxColor)
            visualAlgorithmTextRectangle = visualAlgorithmChoiceText.get_rect()
            visualAlgorithmTextRectangle.center = (visualAlgorithmExplanation.center)
            visualAlgorithmChoiceTextRect = visualAlgorithmChoiceText.get_rect(center=visualAlgorithmExplanation.center)
            WINDOWSURFACE.blit(visualAlgorithmChoiceText, visualAlgorithmChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, boxColor, visualAlgorithmExplanation2)
            visualAlgorithmChoiceText2 = font.render("Ring Puzzle using images",
                                                    True, textColor, boxColor)
            visualAlgorithmTextRectangle2 = visualAlgorithmChoiceText2.get_rect()
            visualAlgorithmTextRectangle2.center = (visualAlgorithmExplanation2.center)
            visualAlgorithmChoiceTextRect2 = visualAlgorithmChoiceText2.get_rect(center=visualAlgorithmExplanation2.center)
            WINDOWSURFACE.blit(visualAlgorithmChoiceText2, visualAlgorithmChoiceTextRect2)

            pygame.draw.rect(WINDOWSURFACE, boxColor, visualAlgorithmExplanation3)
            visualAlgorithmChoiceText = font.render("of the ring",
                                                    True, textColor, boxColor)
            visualAlgorithmTextRectangle = visualAlgorithmChoiceText.get_rect()
            visualAlgorithmTextRectangle.center = (visualAlgorithmExplanation3.center)
            visualAlgorithmChoiceTextRect = visualAlgorithmChoiceText.get_rect(center=visualAlgorithmExplanation3.center)
            WINDOWSURFACE.blit(visualAlgorithmChoiceText, visualAlgorithmChoiceTextRect)

        if showExplanation == 2:
            pygame.draw.rect(WINDOWSURFACE, boxColor, visualAlgorithmExplanation)
            visualAlgorithmChoiceText = font.render("Model for the Chinese Ring Puzzle",
                                                        True, textColor, boxColor)
            visualAlgorithmTextRectangle = visualAlgorithmChoiceText.get_rect()
            visualAlgorithmTextRectangle.center = (visualAlgorithmExplanation.center)
            visualAlgorithmChoiceTextRect = visualAlgorithmChoiceText.get_rect(
                center=visualAlgorithmExplanation.center)
            WINDOWSURFACE.blit(visualAlgorithmChoiceText, visualAlgorithmChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, boxColor, visualAlgorithmExplanation2)
            visualAlgorithmChoiceText2 = font.render("using 0 and 1 to represent",
                                                     True, textColor, boxColor)
            visualAlgorithmTextRectangle2 = visualAlgorithmChoiceText2.get_rect()
            visualAlgorithmTextRectangle2.center = (visualAlgorithmExplanation2.center)
            visualAlgorithmChoiceTextRect2 = visualAlgorithmChoiceText2.get_rect(
                center=visualAlgorithmExplanation2.center)
            WINDOWSURFACE.blit(visualAlgorithmChoiceText2, visualAlgorithmChoiceTextRect2)

            pygame.draw.rect(WINDOWSURFACE, boxColor, visualAlgorithmExplanation3)
            visualAlgorithmChoiceText = font.render("if the rings are on or off",
                                                    True, textColor, boxColor)
            visualAlgorithmTextRectangle = visualAlgorithmChoiceText.get_rect()
            visualAlgorithmTextRectangle.center = (visualAlgorithmExplanation3.center)
            visualAlgorithmChoiceTextRect = visualAlgorithmChoiceText.get_rect(
                center=visualAlgorithmExplanation3.center)
            WINDOWSURFACE.blit(visualAlgorithmChoiceText, visualAlgorithmChoiceTextRect)

        for event in pygame.event.get():
            checkTermination(event)
            if event.type == MOUSEMOTION:
                if VisualScreenButton.collidepoint(event.pos):
                    Color1 = NewColor
                    showExplanation = 1
                elif AlgorithmScreenButton.collidepoint(event.pos):
                    Color2 = NewColor
                    showExplanation = 2
                elif settingButton.collidepoint(event.pos):
                    Color3 = NewColor
                else:
                    Color = Color1 = Color2 = Color3 = DefaultColor
                    showExplanation = 0
            if event.type == MOUSEBUTTONDOWN:
                if VisualScreenButton.collidepoint(event.pos):
                    VisualStepByStepScreen()
                elif AlgorithmScreenButton.collidepoint(event.pos):
                    AlgorithmStepByStepScreen()
                elif settingButton.collidepoint(event.pos):
                    colorSetting()
        RefreshScreen()


def colorSetting():
    global WINDOWSURFACE, backgroundColor, textColor, secondaryColor, boxColor, oldSecondaryColor, oldBoxColor
    Color1 = Color2 = Color3 = Color4 = Color5 = boxColor
    DefaultColor = boxColor
    NewColor = secondaryColor
    while True:
        if Color3 == secondaryColor:
            Color2 = Color1 = Color4 = Color5 = boxColor
        if Color4 == oldSecondaryColor:
            Color4 = secondaryColor
        WINDOWSURFACE.fill(BLACK)
        pygame.draw.rect(WINDOWSURFACE, backgroundColor, HomeScreenRectangle)

        pygame.draw.rect(WINDOWSURFACE, Color5, BackButton)
        BackChoiceText = font.render("Back", True, textColor, Color5)
        BackTextRectangle = BackChoiceText.get_rect()
        BackTextRectangle.center = (BackButton.center)
        BackChoiceTextRect = BackChoiceText.get_rect(center=BackButton.center)
        WINDOWSURFACE.blit(BackChoiceText, BackChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, WHITE, whiteButton)
        whiteChoiceText = font.render("White", True, BLACK, WHITE)
        whiteTextRectangle = whiteChoiceText.get_rect()
        whiteTextRectangle.center = (whiteButton.center)
        whiteChoiceTextRect = whiteChoiceText.get_rect(center=whiteButton.center)
        WINDOWSURFACE.blit(whiteChoiceText, whiteChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, BLACK, blackButton)
        blackChoiceText = font.render("Black", True, WHITE, BLACK)
        blackTextRectangle = blackChoiceText.get_rect()
        blackTextRectangle.center = (blackButton.center)
        blackChoiceTextRect = blackChoiceText.get_rect(center=blackButton.center)
        WINDOWSURFACE.blit(blackChoiceText, blackChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, GREY, greyButton)
        greyChoiceText = font.render("GREY", True, WHITE, GREY)
        greyTextRectangle = greyChoiceText.get_rect()
        greyTextRectangle.center = (greyButton.center)
        greyChoiceTextRect = greyChoiceText.get_rect(center=greyButton.center)
        WINDOWSURFACE.blit(greyChoiceText, greyChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, RED, redButton)
        redChoiceText = font.render("Red", True, WHITE, RED)
        redTextRectangle = redChoiceText.get_rect()
        redTextRectangle.center = (redButton.center)
        redChoiceTextRect = redChoiceText.get_rect(center=redButton.center)
        WINDOWSURFACE.blit(redChoiceText, redChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, GREEN, greenButton)
        greenChoiceText = font.render("Green", True, WHITE, GREEN)
        greenTextRectangle = greenChoiceText.get_rect()
        greenTextRectangle.center = (greenButton.center)
        greenChoiceTextRect = greenChoiceText.get_rect(center=greenButton.center)
        WINDOWSURFACE.blit(greenChoiceText, greenChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, BLUE, blueButton)
        blueChoiceText = font.render("Blue", True, WHITE, BLUE)
        blueTextRectangle = blueChoiceText.get_rect()
        blueTextRectangle.center = (blueButton.center)
        blueChoiceTextRect = blueChoiceText.get_rect(center=blueButton.center)
        WINDOWSURFACE.blit(blueChoiceText, blueChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, LIGHTBLUE, lightBlueButton)
        lightBlueChoiceText = font.render("Light Blue", True, WHITE, LIGHTBLUE)
        lightBlueTextRectangle = lightBlueChoiceText.get_rect()
        lightBlueTextRectangle.center = (lightBlueButton.center)
        lightBlueChoiceTextRect = lightBlueChoiceText.get_rect(center=lightBlueButton.center)
        WINDOWSURFACE.blit(lightBlueChoiceText, lightBlueChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, PINK, pinkButton)
        pinkChoiceText = font.render("Pink", True, WHITE, PINK)
        pinkTextRectangle = pinkChoiceText.get_rect()
        pinkTextRectangle.center = (pinkButton.center)
        pinkChoiceTextRect = pinkChoiceText.get_rect(center=pinkButton.center)
        WINDOWSURFACE.blit(pinkChoiceText, pinkChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, GOLD, goldButton)
        goldChoiceText = font.render("Gold", True, WHITE, GOLD)
        goldTextRectangle = goldChoiceText.get_rect()
        goldTextRectangle.center = (goldButton.center)
        goldChoiceTextRect = goldChoiceText.get_rect(center=goldButton.center)
        WINDOWSURFACE.blit(goldChoiceText, goldChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, Color1, backgroundColorTab)
        backgroundColorChoiceText = font.render("Background", True, textColor, Color1)
        backgroundColorTextRectangle = backgroundColorChoiceText.get_rect()
        backgroundColorTextRectangle.center = (backgroundColorTab.center)
        backgroundColorChoiceTextRect = backgroundColorChoiceText.get_rect(center=backgroundColorTab.center)
        WINDOWSURFACE.blit(backgroundColorChoiceText, backgroundColorChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, Color2, textColorTab)
        textColorChoiceText = font.render("Text", True, textColor, Color2)
        textColorTextRectangle = textColorChoiceText.get_rect()
        textColorTextRectangle.center = (textColorTab.center)
        textColorChoiceTextRect = textColorChoiceText.get_rect(center=textColorTab.center)
        WINDOWSURFACE.blit(textColorChoiceText, textColorChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, Color3, boxColorTab)
        boxColorChoiceText = font.render("Box", True, textColor, Color3)
        boxColorTextRectangle = boxColorChoiceText.get_rect()
        boxColorTextRectangle.center = (boxColorTab.center)
        boxColorChoiceTextRect = boxColorChoiceText.get_rect(center=boxColorTab.center)
        WINDOWSURFACE.blit(boxColorChoiceText, boxColorChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, Color4, secondaryBoxColorTab)
        secondaryTextColorChoiceText = font.render("Secondary", True, textColor, Color4)
        secondaryTextColorTextRectangle = secondaryTextColorChoiceText.get_rect()
        secondaryTextColorTextRectangle.center = (secondaryBoxColorTab.center)
        secondaryTextColorChoiceTextRect = secondaryTextColorChoiceText.get_rect(center=secondaryBoxColorTab.center)
        WINDOWSURFACE.blit(secondaryTextColorChoiceText, secondaryTextColorChoiceTextRect)

        for event in pygame.event.get():
            checkTermination(event)
            if event.type == MOUSEMOTION:
                if BackButton.collidepoint(event.pos):
                    Color5 = NewColor
            if event.type == MOUSEBUTTONDOWN:
                if BackButton.collidepoint(event.pos):
                    return
                elif backgroundColorTab.collidepoint(event.pos):
                    Color1 = secondaryColor
                    Color2 = Color3 = Color4 = boxColor
                elif textColorTab.collidepoint(event.pos):
                    Color2 = secondaryColor
                    Color1 = Color3 = Color4 = boxColor
                elif boxColorTab.collidepoint(event.pos):
                    Color3 = secondaryColor
                    Color2 = Color4 = Color1 = boxColor
                elif secondaryBoxColorTab.collidepoint(event.pos):
                    Color4 = secondaryColor
                    Color2 = Color3 = Color1 = boxColor
                elif whiteButton.collidepoint(event.pos) and Color1 == secondaryColor:
                    backgroundColor = WHITE
                elif blackButton.collidepoint(event.pos) and Color1 == secondaryColor:
                    backgroundColor = BLACK
                elif greyButton.collidepoint(event.pos) and Color1 == secondaryColor:
                    backgroundColor = GREY
                elif redButton.collidepoint(event.pos) and Color1 == secondaryColor:
                    backgroundColor = RED
                elif greenButton.collidepoint(event.pos) and Color1 == secondaryColor:
                    backgroundColor = GREEN
                elif blueButton.collidepoint(event.pos) and Color1 == secondaryColor:
                    backgroundColor = BLUE
                elif pinkButton.collidepoint(event.pos) and Color1 == secondaryColor:
                    backgroundColor = PINK
                elif goldButton.collidepoint(event.pos) and Color1 == secondaryColor:
                    backgroundColor = GOLD
                elif lightBlueButton.collidepoint(event.pos) and Color1 == secondaryColor:
                    backgroundColor = LIGHTBLUE

                elif whiteButton.collidepoint(event.pos) and Color2 == secondaryColor:
                    textColor = WHITE
                elif blackButton.collidepoint(event.pos) and Color2 == secondaryColor:
                    textColor = BLACK
                elif greyButton.collidepoint(event.pos) and Color2 == secondaryColor:
                    textColor = GREY
                elif redButton.collidepoint(event.pos) and Color2 == secondaryColor:
                    textColor = RED
                elif greenButton.collidepoint(event.pos) and Color2 == secondaryColor:
                    textColor = GREEN
                elif blueButton.collidepoint(event.pos) and Color2 == secondaryColor:
                    textColor = BLUE
                elif pinkButton.collidepoint(event.pos) and Color2 == secondaryColor:
                    textColor = PINK
                elif goldButton.collidepoint(event.pos) and Color2 == secondaryColor:
                    textColor = GOLD
                elif lightBlueButton.collidepoint(event.pos) and Color2 == secondaryColor:
                    textColor = LIGHTBLUE

                elif whiteButton.collidepoint(event.pos) and Color3 == secondaryColor and secondaryColor != WHITE:
                    oldBoxColor = boxColor
                    boxColor = WHITE
                elif blackButton.collidepoint(event.pos) and Color3 == secondaryColor and secondaryColor != BLACK:
                    oldBoxColor = boxColor
                    boxColor = BLACK
                elif greyButton.collidepoint(event.pos) and Color3 == secondaryColor and secondaryColor != GREY:
                    oldBoxColor = boxColor
                    boxColor = GREY
                elif redButton.collidepoint(event.pos) and Color3 == secondaryColor and secondaryColor != RED:
                    oldBoxColor = boxColor
                    boxColor = RED
                elif greenButton.collidepoint(event.pos) and Color3 == secondaryColor and secondaryColor != GREEN:
                    oldBoxColor = boxColor
                    boxColor = GREEN
                elif blueButton.collidepoint(event.pos) and Color3 == secondaryColor and secondaryColor != BLUE:
                    oldBoxColor = boxColor
                    boxColor = BLUE
                elif pinkButton.collidepoint(event.pos) and Color3 == secondaryColor and secondaryColor != PINK:
                    oldBoxColor = boxColor
                    boxColor = PINK
                elif goldButton.collidepoint(event.pos) and Color3 == secondaryColor and secondaryColor != GOLD:
                    oldBoxColor = boxColor
                    boxColor = GOLD
                elif lightBlueButton.collidepoint(event.pos) and Color3 == secondaryColor and secondaryColor != LIGHTBLUE:
                    oldBoxColor = boxColor
                    boxColor = LIGHTBLUE

                elif whiteButton.collidepoint(event.pos) and Color4 == secondaryColor and boxColor != WHITE:
                    oldSecondaryColor = secondaryColor
                    secondaryColor = WHITE
                elif blackButton.collidepoint(event.pos) and Color4 == secondaryColor and boxColor != BLACK:
                    oldSecondaryColor = secondaryColor
                    secondaryColor = BLACK
                elif greyButton.collidepoint(event.pos) and Color4 == secondaryColor and boxColor != GREY:
                    oldSecondaryColor = secondaryColor
                    secondaryColor = GREY
                elif redButton.collidepoint(event.pos) and Color4 == secondaryColor and boxColor != RED:
                    oldSecondaryColor = secondaryColor
                    secondaryColor = RED
                elif greenButton.collidepoint(event.pos) and Color4 == secondaryColor and boxColor != GREEN:
                    oldSecondaryColor = secondaryColor
                    secondaryColor = GREEN
                elif blueButton.collidepoint(event.pos) and Color4 == secondaryColor and boxColor != BLUE:
                    oldSecondaryColor = secondaryColor
                    secondaryColor = BLUE
                elif pinkButton.collidepoint(event.pos) and Color4 == secondaryColor and boxColor != PINK:
                    oldSecondaryColor = secondaryColor
                    secondaryColor = PINK
                elif goldButton.collidepoint(event.pos) and Color4 == secondaryColor  and boxColor != GOLD:
                    oldSecondaryColor = secondaryColor
                    secondaryColor = GOLD
                elif lightBlueButton.collidepoint(event.pos) and Color4 == secondaryColor and boxColor != LIGHTBLUE:
                    oldSecondaryColor = secondaryColor
                    secondaryColor = LIGHTBLUE
        RefreshScreen()

def greySteps(i):
    if (i == 1):
        return ["0", "1"]
    previous = greySteps(i - 1)
    updated, new = [], []
    for step in previous:
        updated.append("0" + step)
        new.append("1" + step)
    return updated + new[::-1]


# Recursive function to solve the rings
def solveRings(i):
    steps = greySteps(i)[::-1]
    for j in range(len(steps)):
        if steps[j] == "1" * i:
            return (steps[j:])

def VisualStepByStepScreen():
    global WINDOWSURFACE, backgroundColor, textColor, secondaryColor, oldBoxColor
    Color1 = Color2 = Color3 = Color4 = boxColor
    DefaultColor = boxColor
    NewColor = secondaryColor
    onX1 = 3*WINDOWWIDTH/15
    onX2 = 4 * WINDOWWIDTH / 15
    onX3 = 5 * WINDOWWIDTH / 15
    onX4 = 6 * WINDOWWIDTH / 15
    onX5 = 7 * WINDOWWIDTH / 15
    onX6 = 8 * WINDOWWIDTH / 15
    onX7 = 9 * WINDOWWIDTH / 15
    onX8 = 10 * WINDOWWIDTH / 15
    onX9 = 11 * WINDOWWIDTH / 15
    onY = 3*WINDOWHEIGHT/10 - 10
    offX1 = 3 * WINDOWWIDTH/15
    offX2 = 4 * WINDOWWIDTH / 15
    offX3 = 5 * WINDOWWIDTH / 15
    offX4 = 6 * WINDOWWIDTH / 15
    offX5 = 7 * WINDOWWIDTH / 15
    offX6 = 8 * WINDOWWIDTH / 15
    offX7 = 9 * WINDOWWIDTH / 15
    offX8 = 10 * WINDOWWIDTH / 15
    offX9 = 11 * WINDOWWIDTH / 15
    offY = 4.5*WINDOWHEIGHT/10 - 10
    if NumberChosen % 2 == 1:
        numberOfMoves = (2**(NumberChosen+1)-1)/3
    if NumberChosen % 2 == 0:
        numberOfMoves = (2**(NumberChosen+1)-2)/3
    RingPuzzleSet1 = [1]
    RingPuzzleSet2 = [1, 1]
    RingPuzzleSet3 = [1, 1, 1]
    RingPuzzleSet4 = [1, 1, 1, 1]
    RingPuzzleSet5 = [1, 1, 1, 1, 1]
    RingPuzzleSet6 = [1, 1, 1, 1, 1, 1]
    RingPuzzleSet7 = [1, 1, 1, 1, 1, 1, 1]
    RingPuzzleSet8 = [1, 1, 1, 1, 1, 1, 1, 1]
    RingPuzzleSet9 = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    yCord1 = onY
    yCord2 = onY
    yCord3 = onY
    yCord4 = onY
    yCord5 = onY
    yCord6 = onY
    yCord7 = onY
    yCord8 = onY
    yCord9 = onY
    oddN = 4
    evenN = 3
    j = 0

    while True:
        if Color1 == oldBoxColor or Color2 == oldBoxColor or Color3 == oldBoxColor or Color4 == oldBoxColor:
            Color1 = Color2 = Color3 = Color4 = boxColor
        WINDOWSURFACE.fill(BLACK)
        pygame.draw.rect(WINDOWSURFACE, backgroundColor, HomeScreenRectangle)

        pygame.draw.rect(WINDOWSURFACE, Color2, BackButton)
        BackChoiceText = font.render("Back", True, textColor, Color2)
        BackTextRectangle = BackChoiceText.get_rect()
        BackTextRectangle.center = (BackButton.center)
        BackChoiceTextRect = BackChoiceText.get_rect(center=BackButton.center)
        WINDOWSURFACE.blit(BackChoiceText, BackChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, boxColor, FrontToBackScreenButton)
        FrontToBackChoiceText = font.render("Front <---> Back", True, textColor, boxColor)
        FrontToBackTextRectangle = FrontToBackChoiceText.get_rect()
        FrontToBackTextRectangle.center = (FrontToBackScreenButton.center)
        FrontToBackChoiceTextRect = FrontToBackChoiceText.get_rect(center=FrontToBackScreenButton.center)
        WINDOWSURFACE.blit(FrontToBackChoiceText, FrontToBackChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, boxColor, OnRodButton)
        OnRodChoiceText = font.render("On Rod", True, textColor, boxColor)
        OnRodTextRectangle = OnRodChoiceText.get_rect()
        OnRodTextRectangle.center = (OnRodButton.center)
        OnRodChoiceTextRect = OnRodChoiceText.get_rect(center=OnRodButton.center)
        WINDOWSURFACE.blit(OnRodChoiceText, OnRodChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, boxColor, OffRodButton)
        OffRodChoiceText = font.render("Off Rod", True, textColor, boxColor)
        OffRodTextRectangle = OffRodChoiceText.get_rect()
        OffRodTextRectangle.center = (OffRodButton.center)
        OffRodChoiceTextRect = OffRodChoiceText.get_rect(center=OffRodButton.center)
        WINDOWSURFACE.blit(OffRodChoiceText, OffRodChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, Color4, NextStepButton)
        NextStepChoiceText = font.render("Next Step", True, textColor, Color4)
        NextStepTextRectangle = NextStepChoiceText.get_rect()
        NextStepTextRectangle.center = (NextStepButton.center)
        NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=NextStepButton.center)
        WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, Color1, nameCredit)
        nameCreditChoiceText = smallFont.render("by Taiki Nagao", True, textColor, Color1)
        nameCreditTextRectangle = nameCreditChoiceText.get_rect()
        nameCreditTextRectangle.center = (nameCredit.center)
        nameCreditChoiceTextRect = nameCreditChoiceText.get_rect(center=nameCredit.center)
        WINDOWSURFACE.blit(nameCreditChoiceText, nameCreditChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, Color1, courseCredit)
        courseCreditChoiceText = smallFont.render("MVC and Linear Algebra", True, textColor, Color1)
        courseCreditTextRectangle = courseCreditChoiceText.get_rect()
        courseCreditTextRectangle.center = (courseCredit.center)
        courseCreditChoiceTextRect = courseCreditChoiceText.get_rect(center=courseCredit.center)
        WINDOWSURFACE.blit(courseCreditChoiceText, courseCreditChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, Color3, settingButton)
        settingButtonChoiceText = font.render("Setting", True, textColor, Color3)
        settingButtonTextRectangle = settingButtonChoiceText.get_rect()
        settingButtonTextRectangle.center = (settingButton.center)
        settingButtonChoiceTextRect = settingButtonChoiceText.get_rect(center=settingButton.center)
        WINDOWSURFACE.blit(settingButtonChoiceText, settingButtonChoiceTextRect)

        if NumberChosen == 1:
            RingRectangle1 = pygame.Rect(onX1, yCord1, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage1 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle1.width, RingRectangle1.height))
            WINDOWSURFACE.blit(RingImage1, RingRectangle1)

            for event in pygame.event.get():
                checkTermination(event)
                if event.type == MOUSEMOTION:
                    if BackButton.collidepoint(event.pos):
                        Color2 = NewColor
                    elif settingButton.collidepoint(event.pos):
                        Color3 = NewColor
                    elif NextStepButton.collidepoint(event.pos):
                        Color4 = NewColor
                    else:
                        Color1 = Color2 = Color3 = Color4 = DefaultColor
                if event.type == MOUSEBUTTONDOWN:
                    if settingButton.collidepoint(event.pos):
                        colorSetting()
                    if BackButton.collidepoint(event.pos):
                        return
                    if NextStepButton.collidepoint(event.pos):

                        numberOfRings = NumberChosen
                        if RingPuzzleSet9[0] == 0 and RingPuzzleSet9[1] == 0 and RingPuzzleSet9[2] == 0 and \
                                RingPuzzleSet9[3] == 0 and RingPuzzleSet9[4] == 0 and RingPuzzleSet9[5] == 0 and \
                                RingPuzzleSet9[6] == 0 and RingPuzzleSet9[7] == 0 and RingPuzzleSet9[8] == 0:
                            RingPuzzleSet9[0] = 0
                            yCord1 = offY
                        else:
                            j = int(j) + 1
                            x = [int(a) for a in str(solveRings(NumberChosen)[j - 1])]
                            for k in range(NumberChosen):
                                numberOfRings = numberOfRings - 1
                                newX = x[k]
                                if newX == 0:
                                    RingPuzzleSet9[numberOfRings] = 0
                                if newX == 1:
                                    RingPuzzleSet9[numberOfRings] = 1
                                if RingPuzzleSet9[0] == 0:
                                    yCord1 = offY
                                if RingPuzzleSet9[0] == 1:
                                    yCord1 = onY
                                if RingPuzzleSet9[1] == 0:
                                    yCord2 = offY
                                if RingPuzzleSet9[1] == 1:
                                    yCord2 = onY
                                if RingPuzzleSet9[2] == 0:
                                    yCord3 = offY
                                if RingPuzzleSet9[2] == 1:
                                    yCord3 = onY
                                if RingPuzzleSet9[3] == 0:
                                    yCord4 = offY
                                if RingPuzzleSet9[3] == 1:
                                    yCord4 = onY
                                if RingPuzzleSet9[4] == 0:
                                    yCord5 = offY
                                if RingPuzzleSet9[4] == 1:
                                    yCord5 = onY
                                if RingPuzzleSet9[5] == 0:
                                    yCord6 = offY
                                if RingPuzzleSet9[5] == 1:
                                    yCord6 = onY
                                if RingPuzzleSet9[6] == 0:
                                    yCord7 = offY
                                if RingPuzzleSet9[6] == 1:
                                    yCord7 = onY
                                if RingPuzzleSet9[7] == 0:
                                    yCord8 = offY
                                if RingPuzzleSet9[7] == 1:
                                    yCord8 = onY
                                if RingPuzzleSet9[8] == 0:
                                    yCord9 = offY
                                if RingPuzzleSet9[8] == 1:
                                    yCord9 = onY

        if NumberChosen == 2:
            RingRectangle1 = pygame.Rect(onX1, yCord1, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage1 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle1.width, RingRectangle1.height))
            WINDOWSURFACE.blit(RingImage1, RingRectangle1)

            RingRectangle2 = pygame.Rect(onX2, yCord2, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage2 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle2.width, RingRectangle2.height))
            WINDOWSURFACE.blit(RingImage2, RingRectangle2)
            for event in pygame.event.get():
                checkTermination(event)
                if event.type == MOUSEMOTION:
                    if BackButton.collidepoint(event.pos):
                        Color2 = NewColor
                    elif settingButton.collidepoint(event.pos):
                        Color3 = NewColor
                    else:
                        Color1 = Color2 = Color3 = DefaultColor
                if event.type == MOUSEBUTTONDOWN:
                    if settingButton.collidepoint(event.pos):
                        colorSetting()
                    if BackButton.collidepoint(event.pos):
                        return
                    if NextStepButton.collidepoint(event.pos):

                        numberOfRings = NumberChosen
                        if RingPuzzleSet9[0] == 0 and RingPuzzleSet9[1] == 0 and RingPuzzleSet9[2] == 0 and \
                                RingPuzzleSet9[3] == 0 and RingPuzzleSet9[4] == 0 and RingPuzzleSet9[5] == 0 and \
                                RingPuzzleSet9[6] == 0 and RingPuzzleSet9[7] == 0 and RingPuzzleSet9[8] == 0:
                            RingPuzzleSet9[0] = 0
                            yCord1 = offY
                        else:
                            j = int(j) + 1
                            x = [int(a) for a in str(solveRings(NumberChosen)[j - 1])]
                            for k in range(NumberChosen):
                                numberOfRings = numberOfRings - 1
                                newX = x[k]
                                if newX == 0:
                                    RingPuzzleSet9[numberOfRings] = 0
                                if newX == 1:
                                    RingPuzzleSet9[numberOfRings] = 1
                                if RingPuzzleSet9[0] == 0:
                                    yCord1 = offY
                                if RingPuzzleSet9[0] == 1:
                                    yCord1 = onY
                                if RingPuzzleSet9[1] == 0:
                                    yCord2 = offY
                                if RingPuzzleSet9[1] == 1:
                                    yCord2 = onY
                                if RingPuzzleSet9[2] == 0:
                                    yCord3 = offY
                                if RingPuzzleSet9[2] == 1:
                                    yCord3 = onY
                                if RingPuzzleSet9[3] == 0:
                                    yCord4 = offY
                                if RingPuzzleSet9[3] == 1:
                                    yCord4 = onY
                                if RingPuzzleSet9[4] == 0:
                                    yCord5 = offY
                                if RingPuzzleSet9[4] == 1:
                                    yCord5 = onY
                                if RingPuzzleSet9[5] == 0:
                                    yCord6 = offY
                                if RingPuzzleSet9[5] == 1:
                                    yCord6 = onY
                                if RingPuzzleSet9[6] == 0:
                                    yCord7 = offY
                                if RingPuzzleSet9[6] == 1:
                                    yCord7 = onY
                                if RingPuzzleSet9[7] == 0:
                                    yCord8 = offY
                                if RingPuzzleSet9[7] == 1:
                                    yCord8 = onY
                                if RingPuzzleSet9[8] == 0:
                                    yCord9 = offY
                                if RingPuzzleSet9[8] == 1:
                                    yCord9 = onY

        if NumberChosen == 3:
            RingRectangle1 = pygame.Rect(onX1, yCord1, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage1 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle1.width, RingRectangle1.height))
            WINDOWSURFACE.blit(RingImage1, RingRectangle1)

            RingRectangle2 = pygame.Rect(onX2, yCord2, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage2 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle2.width, RingRectangle2.height))
            WINDOWSURFACE.blit(RingImage2, RingRectangle2)

            RingRectangle3 = pygame.Rect(onX3, yCord3, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage3 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle3.width, RingRectangle3.height))
            WINDOWSURFACE.blit(RingImage3, RingRectangle3)

            for event in pygame.event.get():
                checkTermination(event)
                if event.type == MOUSEMOTION:
                    if BackButton.collidepoint(event.pos):
                        Color2 = NewColor
                    elif settingButton.collidepoint(event.pos):
                        Color3 = NewColor
                    else:
                        Color1 = Color2 = Color3 = DefaultColor
                if event.type == MOUSEBUTTONDOWN:
                    if settingButton.collidepoint(event.pos):
                        colorSetting()
                    if BackButton.collidepoint(event.pos):
                        return
                    if NextStepButton.collidepoint(event.pos):

                        numberOfRings = NumberChosen
                        if RingPuzzleSet9[0] == 0 and RingPuzzleSet9[1] == 0 and RingPuzzleSet9[2] == 0 and \
                                RingPuzzleSet9[3] == 0 and RingPuzzleSet9[4] == 0 and RingPuzzleSet9[5] == 0 and \
                                RingPuzzleSet9[6] == 0 and RingPuzzleSet9[7] == 0 and RingPuzzleSet9[8] == 0:
                            RingPuzzleSet9[0] = 0
                            yCord1 = offY
                        else:
                            j = int(j) + 1
                            x = [int(a) for a in str(solveRings(NumberChosen)[j - 1])]
                            for k in range(NumberChosen):
                                numberOfRings = numberOfRings - 1
                                newX = x[k]
                                if newX == 0:
                                    RingPuzzleSet9[numberOfRings] = 0
                                if newX == 1:
                                    RingPuzzleSet9[numberOfRings] = 1
                                if RingPuzzleSet9[0] == 0:
                                    yCord1 = offY
                                if RingPuzzleSet9[0] == 1:
                                    yCord1 = onY
                                if RingPuzzleSet9[1] == 0:
                                    yCord2 = offY
                                if RingPuzzleSet9[1] == 1:
                                    yCord2 = onY
                                if RingPuzzleSet9[2] == 0:
                                    yCord3 = offY
                                if RingPuzzleSet9[2] == 1:
                                    yCord3 = onY
                                if RingPuzzleSet9[3] == 0:
                                    yCord4 = offY
                                if RingPuzzleSet9[3] == 1:
                                    yCord4 = onY
                                if RingPuzzleSet9[4] == 0:
                                    yCord5 = offY
                                if RingPuzzleSet9[4] == 1:
                                    yCord5 = onY
                                if RingPuzzleSet9[5] == 0:
                                    yCord6 = offY
                                if RingPuzzleSet9[5] == 1:
                                    yCord6 = onY
                                if RingPuzzleSet9[6] == 0:
                                    yCord7 = offY
                                if RingPuzzleSet9[6] == 1:
                                    yCord7 = onY
                                if RingPuzzleSet9[7] == 0:
                                    yCord8 = offY
                                if RingPuzzleSet9[7] == 1:
                                    yCord8 = onY
                                if RingPuzzleSet9[8] == 0:
                                    yCord9 = offY
                                if RingPuzzleSet9[8] == 1:
                                    yCord9 = onY

        if NumberChosen == 4:
            RingRectangle1 = pygame.Rect(onX1, yCord1, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage1 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle1.width, RingRectangle1.height))
            WINDOWSURFACE.blit(RingImage1, RingRectangle1)

            RingRectangle2 = pygame.Rect(onX2, yCord2, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage2 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle2.width, RingRectangle2.height))
            WINDOWSURFACE.blit(RingImage2, RingRectangle2)

            RingRectangle3 = pygame.Rect(onX3, yCord3, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage3 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle3.width, RingRectangle3.height))
            WINDOWSURFACE.blit(RingImage3, RingRectangle3)

            RingRectangle4 = pygame.Rect(onX4, yCord4, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage4 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle4.width, RingRectangle4.height))
            WINDOWSURFACE.blit(RingImage4, RingRectangle4)
            for event in pygame.event.get():
                checkTermination(event)
                if event.type == MOUSEMOTION:
                    if BackButton.collidepoint(event.pos):
                        Color2 = NewColor
                    elif settingButton.collidepoint(event.pos):
                        Color3 = NewColor
                    else:
                        Color1 = Color2 = Color3 = DefaultColor
                if event.type == MOUSEBUTTONDOWN:
                    if settingButton.collidepoint(event.pos):
                        colorSetting()
                    if BackButton.collidepoint(event.pos):
                        return
                    if NextStepButton.collidepoint(event.pos):

                        numberOfRings = NumberChosen
                        if RingPuzzleSet9[0] == 0 and RingPuzzleSet9[1] == 0 and RingPuzzleSet9[2] == 0 and \
                                RingPuzzleSet9[3] == 0 and RingPuzzleSet9[4] == 0 and RingPuzzleSet9[5] == 0 and \
                                RingPuzzleSet9[6] == 0 and RingPuzzleSet9[7] == 0 and RingPuzzleSet9[8] == 0:
                            RingPuzzleSet9[0] = 0
                            yCord1 = offY
                        else:
                            j = int(j) + 1
                            x = [int(a) for a in str(solveRings(NumberChosen)[j - 1])]
                            for k in range(NumberChosen):
                                numberOfRings = numberOfRings - 1
                                newX = x[k]
                                if newX == 0:
                                    RingPuzzleSet9[numberOfRings] = 0
                                if newX == 1:
                                    RingPuzzleSet9[numberOfRings] = 1
                                if RingPuzzleSet9[0] == 0:
                                    yCord1 = offY
                                if RingPuzzleSet9[0] == 1:
                                    yCord1 = onY
                                if RingPuzzleSet9[1] == 0:
                                    yCord2 = offY
                                if RingPuzzleSet9[1] == 1:
                                    yCord2 = onY
                                if RingPuzzleSet9[2] == 0:
                                    yCord3 = offY
                                if RingPuzzleSet9[2] == 1:
                                    yCord3 = onY
                                if RingPuzzleSet9[3] == 0:
                                    yCord4 = offY
                                if RingPuzzleSet9[3] == 1:
                                    yCord4 = onY
                                if RingPuzzleSet9[4] == 0:
                                    yCord5 = offY
                                if RingPuzzleSet9[4] == 1:
                                    yCord5 = onY
                                if RingPuzzleSet9[5] == 0:
                                    yCord6 = offY
                                if RingPuzzleSet9[5] == 1:
                                    yCord6 = onY
                                if RingPuzzleSet9[6] == 0:
                                    yCord7 = offY
                                if RingPuzzleSet9[6] == 1:
                                    yCord7 = onY
                                if RingPuzzleSet9[7] == 0:
                                    yCord8 = offY
                                if RingPuzzleSet9[7] == 1:
                                    yCord8 = onY
                                if RingPuzzleSet9[8] == 0:
                                    yCord9 = offY
                                if RingPuzzleSet9[8] == 1:
                                    yCord9 = onY

        if NumberChosen == 5:
            RingRectangle1 = pygame.Rect(onX1, yCord1, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage1 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle1.width, RingRectangle1.height))
            WINDOWSURFACE.blit(RingImage1, RingRectangle1)

            RingRectangle2 = pygame.Rect(onX2, yCord2, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage2 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle2.width, RingRectangle2.height))
            WINDOWSURFACE.blit(RingImage2, RingRectangle2)

            RingRectangle3 = pygame.Rect(onX3, yCord3, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage3 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle3.width, RingRectangle3.height))
            WINDOWSURFACE.blit(RingImage3, RingRectangle3)

            RingRectangle4 = pygame.Rect(onX4, yCord4, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage4 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle4.width, RingRectangle4.height))
            WINDOWSURFACE.blit(RingImage4, RingRectangle4)

            RingRectangle5 = pygame.Rect(onX5, yCord5, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage5 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle5.width, RingRectangle5.height))
            WINDOWSURFACE.blit(RingImage5, RingRectangle5)

            for event in pygame.event.get():
                checkTermination(event)
                if event.type == MOUSEMOTION:
                    if BackButton.collidepoint(event.pos):
                        Color2 = NewColor
                    elif settingButton.collidepoint(event.pos):
                        Color3 = NewColor
                    else:
                        Color1 = Color2 = Color3 = DefaultColor
                if event.type == MOUSEBUTTONDOWN:
                    if settingButton.collidepoint(event.pos):
                        colorSetting()
                    if BackButton.collidepoint(event.pos):
                        return
                    if NextStepButton.collidepoint(event.pos):

                        numberOfRings = NumberChosen
                        if RingPuzzleSet9[0] == 0 and RingPuzzleSet9[1] == 0 and RingPuzzleSet9[2] == 0 and \
                                RingPuzzleSet9[3] == 0 and RingPuzzleSet9[4] == 0 and RingPuzzleSet9[5] == 0 and \
                                RingPuzzleSet9[6] == 0 and RingPuzzleSet9[7] == 0 and RingPuzzleSet9[8] == 0:
                            RingPuzzleSet9[0] = 0
                            yCord1 = offY
                        else:
                            j = int(j) + 1
                            x = [int(a) for a in str(solveRings(NumberChosen)[j - 1])]
                            for k in range(NumberChosen):
                                numberOfRings = numberOfRings - 1
                                newX = x[k]
                                if newX == 0:
                                    RingPuzzleSet9[numberOfRings] = 0
                                if newX == 1:
                                    RingPuzzleSet9[numberOfRings] = 1
                                if RingPuzzleSet9[0] == 0:
                                    yCord1 = offY
                                if RingPuzzleSet9[0] == 1:
                                    yCord1 = onY
                                if RingPuzzleSet9[1] == 0:
                                    yCord2 = offY
                                if RingPuzzleSet9[1] == 1:
                                    yCord2 = onY
                                if RingPuzzleSet9[2] == 0:
                                    yCord3 = offY
                                if RingPuzzleSet9[2] == 1:
                                    yCord3 = onY
                                if RingPuzzleSet9[3] == 0:
                                    yCord4 = offY
                                if RingPuzzleSet9[3] == 1:
                                    yCord4 = onY
                                if RingPuzzleSet9[4] == 0:
                                    yCord5 = offY
                                if RingPuzzleSet9[4] == 1:
                                    yCord5 = onY
                                if RingPuzzleSet9[5] == 0:
                                    yCord6 = offY
                                if RingPuzzleSet9[5] == 1:
                                    yCord6 = onY
                                if RingPuzzleSet9[6] == 0:
                                    yCord7 = offY
                                if RingPuzzleSet9[6] == 1:
                                    yCord7 = onY
                                if RingPuzzleSet9[7] == 0:
                                    yCord8 = offY
                                if RingPuzzleSet9[7] == 1:
                                    yCord8 = onY
                                if RingPuzzleSet9[8] == 0:
                                    yCord9 = offY
                                if RingPuzzleSet9[8] == 1:
                                    yCord9 = onY

        if NumberChosen == 6:
            RingRectangle1 = pygame.Rect(onX1, yCord1, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage1 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle1.width, RingRectangle1.height))
            WINDOWSURFACE.blit(RingImage1, RingRectangle1)

            RingRectangle2 = pygame.Rect(onX2, yCord2, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage2 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle2.width, RingRectangle2.height))
            WINDOWSURFACE.blit(RingImage2, RingRectangle2)

            RingRectangle3 = pygame.Rect(onX3, yCord3, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage3 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle3.width, RingRectangle3.height))
            WINDOWSURFACE.blit(RingImage3, RingRectangle3)

            RingRectangle4 = pygame.Rect(onX4, yCord4, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage4 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle4.width, RingRectangle4.height))
            WINDOWSURFACE.blit(RingImage4, RingRectangle4)

            RingRectangle5 = pygame.Rect(onX5, yCord5, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage5 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle5.width, RingRectangle5.height))
            WINDOWSURFACE.blit(RingImage5, RingRectangle5)

            RingRectangle6 = pygame.Rect(onX6, yCord6, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage6 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle6.width, RingRectangle6.height))
            WINDOWSURFACE.blit(RingImage6, RingRectangle6)
            for event in pygame.event.get():
                checkTermination(event)
                if event.type == MOUSEMOTION:
                    if BackButton.collidepoint(event.pos):
                        Color2 = NewColor
                    elif settingButton.collidepoint(event.pos):
                        Color3 = NewColor
                    else:
                        Color1 = Color2 = Color3 = DefaultColor
                if event.type == MOUSEBUTTONDOWN:
                    if settingButton.collidepoint(event.pos):
                        colorSetting()
                    if BackButton.collidepoint(event.pos):
                        return
                    if NextStepButton.collidepoint(event.pos):

                        numberOfRings = NumberChosen
                        if RingPuzzleSet9[0] == 0 and RingPuzzleSet9[1] == 0 and RingPuzzleSet9[2] == 0 and \
                                RingPuzzleSet9[3] == 0 and RingPuzzleSet9[4] == 0 and RingPuzzleSet9[5] == 0 and \
                                RingPuzzleSet9[6] == 0 and RingPuzzleSet9[7] == 0 and RingPuzzleSet9[8] == 0:
                            RingPuzzleSet9[0] = 0
                            yCord1 = offY
                        else:
                            j = int(j) + 1
                            x = [int(a) for a in str(solveRings(NumberChosen)[j - 1])]
                            for k in range(NumberChosen):
                                numberOfRings = numberOfRings - 1
                                newX = x[k]
                                if newX == 0:
                                    RingPuzzleSet9[numberOfRings] = 0
                                if newX == 1:
                                    RingPuzzleSet9[numberOfRings] = 1
                                if RingPuzzleSet9[0] == 0:
                                    yCord1 = offY
                                if RingPuzzleSet9[0] == 1:
                                    yCord1 = onY
                                if RingPuzzleSet9[1] == 0:
                                    yCord2 = offY
                                if RingPuzzleSet9[1] == 1:
                                    yCord2 = onY
                                if RingPuzzleSet9[2] == 0:
                                    yCord3 = offY
                                if RingPuzzleSet9[2] == 1:
                                    yCord3 = onY
                                if RingPuzzleSet9[3] == 0:
                                    yCord4 = offY
                                if RingPuzzleSet9[3] == 1:
                                    yCord4 = onY
                                if RingPuzzleSet9[4] == 0:
                                    yCord5 = offY
                                if RingPuzzleSet9[4] == 1:
                                    yCord5 = onY
                                if RingPuzzleSet9[5] == 0:
                                    yCord6 = offY
                                if RingPuzzleSet9[5] == 1:
                                    yCord6 = onY
                                if RingPuzzleSet9[6] == 0:
                                    yCord7 = offY
                                if RingPuzzleSet9[6] == 1:
                                    yCord7 = onY
                                if RingPuzzleSet9[7] == 0:
                                    yCord8 = offY
                                if RingPuzzleSet9[7] == 1:
                                    yCord8 = onY
                                if RingPuzzleSet9[8] == 0:
                                    yCord9 = offY
                                if RingPuzzleSet9[8] == 1:
                                    yCord9 = onY


        if NumberChosen == 7:
            RingRectangle1 = pygame.Rect(onX1, yCord1, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage1 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle1.width, RingRectangle1.height))
            WINDOWSURFACE.blit(RingImage1, RingRectangle1)

            RingRectangle2 = pygame.Rect(onX2, yCord2, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage2 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle2.width, RingRectangle2.height))
            WINDOWSURFACE.blit(RingImage2, RingRectangle2)

            RingRectangle3 = pygame.Rect(onX3, yCord3, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage3 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle3.width, RingRectangle3.height))
            WINDOWSURFACE.blit(RingImage3, RingRectangle3)

            RingRectangle4 = pygame.Rect(onX4, yCord4, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage4 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle4.width, RingRectangle4.height))
            WINDOWSURFACE.blit(RingImage4, RingRectangle4)

            RingRectangle5 = pygame.Rect(onX5, yCord5, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage5 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle5.width, RingRectangle5.height))
            WINDOWSURFACE.blit(RingImage5, RingRectangle5)

            RingRectangle6 = pygame.Rect(onX6, yCord6, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage6 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle6.width, RingRectangle6.height))
            WINDOWSURFACE.blit(RingImage6, RingRectangle6)

            RingRectangle7 = pygame.Rect(onX7, yCord7, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage7 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle7.width, RingRectangle7.height))
            WINDOWSURFACE.blit(RingImage7, RingRectangle7)

            for event in pygame.event.get():
                checkTermination(event)
                if event.type == MOUSEMOTION:
                    if BackButton.collidepoint(event.pos):
                        Color2 = NewColor
                    elif settingButton.collidepoint(event.pos):
                        Color3 = NewColor
                    else:
                        Color1 = Color2 = Color3 = DefaultColor
                if event.type == MOUSEBUTTONDOWN:
                    if settingButton.collidepoint(event.pos):
                        colorSetting()
                    if BackButton.collidepoint(event.pos):
                        return
                    if NextStepButton.collidepoint(event.pos):

                        numberOfRings = NumberChosen
                        if RingPuzzleSet9[0] == 0 and RingPuzzleSet9[1] == 0 and RingPuzzleSet9[2] == 0 and \
                                RingPuzzleSet9[3] == 0 and RingPuzzleSet9[4] == 0 and RingPuzzleSet9[5] == 0 and \
                                RingPuzzleSet9[6] == 0 and RingPuzzleSet9[7] == 0 and RingPuzzleSet9[8] == 0:
                            RingPuzzleSet9[0] = 0
                            yCord1 = offY
                        else:
                            j = int(j) + 1
                            x = [int(a) for a in str(solveRings(NumberChosen)[j - 1])]
                            for k in range(NumberChosen):
                                numberOfRings = numberOfRings - 1
                                newX = x[k]
                                if newX == 0:
                                    RingPuzzleSet9[numberOfRings] = 0
                                if newX == 1:
                                    RingPuzzleSet9[numberOfRings] = 1
                                if RingPuzzleSet9[0] == 0:
                                    yCord1 = offY
                                if RingPuzzleSet9[0] == 1:
                                    yCord1 = onY
                                if RingPuzzleSet9[1] == 0:
                                    yCord2 = offY
                                if RingPuzzleSet9[1] == 1:
                                    yCord2 = onY
                                if RingPuzzleSet9[2] == 0:
                                    yCord3 = offY
                                if RingPuzzleSet9[2] == 1:
                                    yCord3 = onY
                                if RingPuzzleSet9[3] == 0:
                                    yCord4 = offY
                                if RingPuzzleSet9[3] == 1:
                                    yCord4 = onY
                                if RingPuzzleSet9[4] == 0:
                                    yCord5 = offY
                                if RingPuzzleSet9[4] == 1:
                                    yCord5 = onY
                                if RingPuzzleSet9[5] == 0:
                                    yCord6 = offY
                                if RingPuzzleSet9[5] == 1:
                                    yCord6 = onY
                                if RingPuzzleSet9[6] == 0:
                                    yCord7 = offY
                                if RingPuzzleSet9[6] == 1:
                                    yCord7 = onY
                                if RingPuzzleSet9[7] == 0:
                                    yCord8 = offY
                                if RingPuzzleSet9[7] == 1:
                                    yCord8 = onY
                                if RingPuzzleSet9[8] == 0:
                                    yCord9 = offY
                                if RingPuzzleSet9[8] == 1:
                                    yCord9 = onY

        if NumberChosen == 8:
            RingRectangle1 = pygame.Rect(onX1, yCord1, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage1 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle1.width, RingRectangle1.height))
            WINDOWSURFACE.blit(RingImage1, RingRectangle1)

            RingRectangle2 = pygame.Rect(onX2, yCord2, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage2 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle2.width, RingRectangle2.height))
            WINDOWSURFACE.blit(RingImage2, RingRectangle2)

            RingRectangle3 = pygame.Rect(onX3, yCord3, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage3 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle3.width, RingRectangle3.height))
            WINDOWSURFACE.blit(RingImage3, RingRectangle3)

            RingRectangle4 = pygame.Rect(onX4, yCord4, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage4 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle4.width, RingRectangle4.height))
            WINDOWSURFACE.blit(RingImage4, RingRectangle4)

            RingRectangle5 = pygame.Rect(onX5, yCord5, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage5 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle5.width, RingRectangle5.height))
            WINDOWSURFACE.blit(RingImage5, RingRectangle5)

            RingRectangle6 = pygame.Rect(onX6, yCord6, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage6 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle6.width, RingRectangle6.height))
            WINDOWSURFACE.blit(RingImage6, RingRectangle6)

            RingRectangle7 = pygame.Rect(onX7, yCord7, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage7 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle7.width, RingRectangle7.height))
            WINDOWSURFACE.blit(RingImage7, RingRectangle7)

            RingRectangle8 = pygame.Rect(onX8, yCord8, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage8 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle8.width, RingRectangle8.height))
            WINDOWSURFACE.blit(RingImage8, RingRectangle8)
            for event in pygame.event.get():
                checkTermination(event)
                if event.type == MOUSEMOTION:
                    if BackButton.collidepoint(event.pos):
                        Color2 = NewColor
                    elif settingButton.collidepoint(event.pos):
                        Color3 = NewColor
                    else:
                        Color1 = Color2 = Color3 = DefaultColor
                if event.type == MOUSEBUTTONDOWN:
                    if settingButton.collidepoint(event.pos):
                        colorSetting()
                    if BackButton.collidepoint(event.pos):
                        return
                    if NextStepButton.collidepoint(event.pos):

                        numberOfRings = NumberChosen
                        if RingPuzzleSet9[0] == 0 and RingPuzzleSet9[1] == 0 and RingPuzzleSet9[2] == 0 and \
                                RingPuzzleSet9[3] == 0 and RingPuzzleSet9[4] == 0 and RingPuzzleSet9[5] == 0 and \
                                RingPuzzleSet9[6] == 0 and RingPuzzleSet9[7] == 0 and RingPuzzleSet9[8] == 0:
                            RingPuzzleSet9[0] = 0
                            yCord1 = offY
                        else:
                            j = int(j) + 1
                            x = [int(a) for a in str(solveRings(NumberChosen)[j - 1])]
                            for k in range(NumberChosen):
                                numberOfRings = numberOfRings - 1
                                newX = x[k]
                                if newX == 0:
                                    RingPuzzleSet9[numberOfRings] = 0
                                if newX == 1:
                                    RingPuzzleSet9[numberOfRings] = 1
                                if RingPuzzleSet9[0] == 0:
                                    yCord1 = offY
                                if RingPuzzleSet9[0] == 1:
                                    yCord1 = onY
                                if RingPuzzleSet9[1] == 0:
                                    yCord2 = offY
                                if RingPuzzleSet9[1] == 1:
                                    yCord2 = onY
                                if RingPuzzleSet9[2] == 0:
                                    yCord3 = offY
                                if RingPuzzleSet9[2] == 1:
                                    yCord3 = onY
                                if RingPuzzleSet9[3] == 0:
                                    yCord4 = offY
                                if RingPuzzleSet9[3] == 1:
                                    yCord4 = onY
                                if RingPuzzleSet9[4] == 0:
                                    yCord5 = offY
                                if RingPuzzleSet9[4] == 1:
                                    yCord5 = onY
                                if RingPuzzleSet9[5] == 0:
                                    yCord6 = offY
                                if RingPuzzleSet9[5] == 1:
                                    yCord6 = onY
                                if RingPuzzleSet9[6] == 0:
                                    yCord7 = offY
                                if RingPuzzleSet9[6] == 1:
                                    yCord7 = onY
                                if RingPuzzleSet9[7] == 0:
                                    yCord8 = offY
                                if RingPuzzleSet9[7] == 1:
                                    yCord8 = onY
                                if RingPuzzleSet9[8] == 0:
                                    yCord9 = offY
                                if RingPuzzleSet9[8] == 1:
                                    yCord9 = onY

        if NumberChosen == 9:
            RingRectangle1 = pygame.Rect(onX1, yCord1, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage1 = pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")), (RingRectangle1.width, RingRectangle1.height))
            WINDOWSURFACE.blit(RingImage1, RingRectangle1)

            RingRectangle2 = pygame.Rect(onX2, yCord2, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage2 = pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")), (RingRectangle2.width, RingRectangle2.height))
            WINDOWSURFACE.blit(RingImage2, RingRectangle2)

            RingRectangle3 = pygame.Rect(onX3, yCord3, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage3 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle3.width, RingRectangle3.height))
            WINDOWSURFACE.blit(RingImage3, RingRectangle3)

            RingRectangle4 = pygame.Rect(onX4, yCord4, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage4 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle4.width, RingRectangle4.height))
            WINDOWSURFACE.blit(RingImage4, RingRectangle4)

            RingRectangle5 = pygame.Rect(onX5, yCord5, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage5 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle5.width, RingRectangle5.height))
            WINDOWSURFACE.blit(RingImage5, RingRectangle5)

            RingRectangle6 = pygame.Rect(onX6, yCord6, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage6 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle6.width, RingRectangle6.height))
            WINDOWSURFACE.blit(RingImage6, RingRectangle6)

            RingRectangle7 = pygame.Rect(onX7, yCord7, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage7 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle7.width, RingRectangle7.height))
            WINDOWSURFACE.blit(RingImage7, RingRectangle7)

            RingRectangle8 = pygame.Rect(onX8, yCord8, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage8 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle8.width, RingRectangle8.height))
            WINDOWSURFACE.blit(RingImage8, RingRectangle8)

            RingRectangle9 = pygame.Rect(onX9, yCord9, int(WINDOWWIDTH / 12), int(WINDOWHEIGHT / 12))
            RingImage9 = pygame.transform.scale(
                pygame.image.load(os.path.join(os.path.dirname(__file__), "Images", "RingPuzzle.png")),
                (RingRectangle9.width, RingRectangle9.height))
            WINDOWSURFACE.blit(RingImage9, RingRectangle9)

            for event in pygame.event.get():
                checkTermination(event)
                if event.type == MOUSEMOTION:
                    if BackButton.collidepoint(event.pos):
                        Color2 = NewColor
                    elif settingButton.collidepoint(event.pos):
                        Color3 = NewColor
                    else:
                        Color1 = Color2 = Color3 = DefaultColor
                if event.type == MOUSEBUTTONDOWN:
                    if settingButton.collidepoint(event.pos):
                        colorSetting()
                    if BackButton.collidepoint(event.pos):
                        return
                    if NextStepButton.collidepoint(event.pos):

                        numberOfRings = NumberChosen
                        if RingPuzzleSet9[0] == 0 and RingPuzzleSet9[1] == 0 and RingPuzzleSet9[2] == 0 and \
                                RingPuzzleSet9[3] == 0 and RingPuzzleSet9[4] == 0 and RingPuzzleSet9[5] == 0 and \
                                RingPuzzleSet9[6] == 0 and RingPuzzleSet9[7] == 0 and RingPuzzleSet9[8] == 0:
                            RingPuzzleSet9[0] = 0
                            yCord1 = offY
                        else:
                            j = int(j) + 1
                            x = [int(a) for a in str(solveRings(NumberChosen)[j - 1])]
                            for k in range(NumberChosen):
                                numberOfRings = numberOfRings - 1
                                newX = x[k]
                                if newX == 0:
                                    RingPuzzleSet9[numberOfRings] = 0
                                if newX == 1:
                                    RingPuzzleSet9[numberOfRings] = 1
                                if RingPuzzleSet9[0] == 0:
                                    yCord1 = offY
                                if RingPuzzleSet9[0] == 1:
                                    yCord1 = onY
                                if RingPuzzleSet9[1] == 0:
                                    yCord2 = offY
                                if RingPuzzleSet9[1] == 1:
                                    yCord2 = onY
                                if RingPuzzleSet9[2] == 0:
                                    yCord3 = offY
                                if RingPuzzleSet9[2] == 1:
                                    yCord3 = onY
                                if RingPuzzleSet9[3] == 0:
                                    yCord4 = offY
                                if RingPuzzleSet9[3] == 1:
                                    yCord4 = onY
                                if RingPuzzleSet9[4] == 0:
                                    yCord5 = offY
                                if RingPuzzleSet9[4] == 1:
                                    yCord5 = onY
                                if RingPuzzleSet9[5] == 0:
                                    yCord6 = offY
                                if RingPuzzleSet9[5] == 1:
                                    yCord6 = onY
                                if RingPuzzleSet9[6] == 0:
                                    yCord7 = offY
                                if RingPuzzleSet9[6] == 1:
                                    yCord7 = onY
                                if RingPuzzleSet9[7] == 0:
                                    yCord8 = offY
                                if RingPuzzleSet9[7] == 1:
                                    yCord8 = onY
                                if RingPuzzleSet9[8] == 0:
                                    yCord9 = offY
                                if RingPuzzleSet9[8] == 1:
                                    yCord9 = onY
        RefreshScreen()


def AlgorithmStepByStepScreen():
    global WINDOWSURFACE, backgroundColor, textColor, secondaryColor, oldBoxColor
    Color1 = Color2 = Color3 = Color4 = boxColor
    DefaultColor = boxColor
    NewColor = secondaryColor
    onX1 = 3 * WINDOWWIDTH / 15
    onX2 = 4 * WINDOWWIDTH / 15
    onX3 = 5 * WINDOWWIDTH / 15
    onX4 = 6 * WINDOWWIDTH / 15
    onX5 = 7 * WINDOWWIDTH / 15
    onX6 = 8 * WINDOWWIDTH / 15
    onX7 = 9 * WINDOWWIDTH / 15
    onX8 = 10 * WINDOWWIDTH / 15
    onX9 = 11 * WINDOWWIDTH / 15
    onY = 3 * WINDOWHEIGHT / 10 - 10
    offX1 = 3 * WINDOWWIDTH / 15
    offX2 = 4 * WINDOWWIDTH / 15
    offX3 = 5 * WINDOWWIDTH / 15
    offX4 = 6 * WINDOWWIDTH / 15
    offX5 = 7 * WINDOWWIDTH / 15
    offX6 = 8 * WINDOWWIDTH / 15
    offX7 = 9 * WINDOWWIDTH / 15
    offX8 = 10 * WINDOWWIDTH / 15
    offX9 = 11 * WINDOWWIDTH / 15
    offY = 4.5 * WINDOWHEIGHT / 10 - 10
    if NumberChosen % 2 == 1:
        numberOfMoves = (2 ** (NumberChosen + 1) - 1) / 3
    if NumberChosen % 2 == 0:
        numberOfMoves = (2 ** (NumberChosen + 1) - 2) / 3
    RingPuzzleSet1 = [1]
    RingPuzzleSet2 = [1, 1]
    RingPuzzleSet3 = [1, 1, 1]
    RingPuzzleSet4 = [1, 1, 1, 1]
    RingPuzzleSet5 = [1, 1, 1, 1, 1]
    RingPuzzleSet6 = [1, 1, 1, 1, 1, 1]
    RingPuzzleSet7 = [1, 1, 1, 1, 1, 1, 1]
    RingPuzzleSet8 = [1, 1, 1, 1, 1, 1, 1, 1]
    RingPuzzleSet9 = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    yCord1 = onY
    yCord2 = onY
    yCord3 = onY
    yCord4 = onY
    yCord5 = onY
    yCord6 = onY
    yCord7 = onY
    yCord8 = onY
    yCord9 = onY
    oddN = 4
    evenN = 3
    j = 0

    while True:
        if Color1 == oldBoxColor or Color2 == oldBoxColor or Color3 == oldBoxColor or Color4 == oldBoxColor:
            Color1 = Color2 = Color3 = Color4 = boxColor
        WINDOWSURFACE.fill(BLACK)
        pygame.draw.rect(WINDOWSURFACE, backgroundColor, HomeScreenRectangle)

        pygame.draw.rect(WINDOWSURFACE, Color2, BackButton)
        BackChoiceText = font.render("Back", True, textColor, Color2)
        BackTextRectangle = BackChoiceText.get_rect()
        BackTextRectangle.center = (BackButton.center)
        BackChoiceTextRect = BackChoiceText.get_rect(center=BackButton.center)
        WINDOWSURFACE.blit(BackChoiceText, BackChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, Color3, settingButton)
        settingButtonChoiceText = font.render("Setting", True, textColor, Color3)
        settingButtonTextRectangle = settingButtonChoiceText.get_rect()
        settingButtonTextRectangle.center = (settingButton.center)
        settingButtonChoiceTextRect = settingButtonChoiceText.get_rect(center=settingButton.center)
        WINDOWSURFACE.blit(settingButtonChoiceText, settingButtonChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, Color4, NextStepButton)
        NextStepChoiceText = font.render("Next Step", True, textColor, Color4)
        NextStepTextRectangle = NextStepChoiceText.get_rect()
        NextStepTextRectangle.center = (NextStepButton.center)
        NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=NextStepButton.center)
        WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, boxColor, FrontToBackScreenButton)
        FrontToBackChoiceText = font.render("Front <---> Back", True, textColor, boxColor)
        FrontToBackTextRectangle = FrontToBackChoiceText.get_rect()
        FrontToBackTextRectangle.center = (FrontToBackScreenButton.center)
        FrontToBackChoiceTextRect = FrontToBackChoiceText.get_rect(center=FrontToBackScreenButton.center)
        WINDOWSURFACE.blit(FrontToBackChoiceText, FrontToBackChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, boxColor, oneExplanation)
        NextStepChoiceText = font.render("0 means off rod", True, textColor, boxColor)
        NextStepTextRectangle = NextStepChoiceText.get_rect()
        NextStepTextRectangle.center = (oneExplanation.center)
        NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=oneExplanation.center)
        WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, boxColor, zeroExplanation)
        NextStepChoiceText = font.render("1 means on rod", True, textColor, boxColor)
        NextStepTextRectangle = NextStepChoiceText.get_rect()
        NextStepTextRectangle.center = (zeroExplanation.center)
        NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=zeroExplanation.center)
        WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, Color1, nameCredit)
        nameCreditChoiceText = smallFont.render("by Taiki Nagao", True, textColor, Color1)
        nameCreditTextRectangle = nameCreditChoiceText.get_rect()
        nameCreditTextRectangle.center = (nameCredit.center)
        nameCreditChoiceTextRect = nameCreditChoiceText.get_rect(center=nameCredit.center)
        WINDOWSURFACE.blit(nameCreditChoiceText, nameCreditChoiceTextRect)

        pygame.draw.rect(WINDOWSURFACE, Color1, courseCredit)
        courseCreditChoiceText = smallFont.render("MVC and Linear Algebra", True, textColor, Color1)
        courseCreditTextRectangle = courseCreditChoiceText.get_rect()
        courseCreditTextRectangle.center = (courseCredit.center)
        courseCreditChoiceTextRect = courseCreditChoiceText.get_rect(center=courseCredit.center)
        WINDOWSURFACE.blit(courseCreditChoiceText, courseCreditChoiceTextRect)

        if NumberChosen == 1:
            pygame.draw.rect(WINDOWSURFACE, backgroundColor, firstRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[0]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (firstRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=firstRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            for event in pygame.event.get():
                checkTermination(event)
                if event.type == MOUSEMOTION:
                    if BackButton.collidepoint(event.pos):
                        Color2 = NewColor
                    elif settingButton.collidepoint(event.pos):
                        Color3 = NewColor
                    elif NextStepButton.collidepoint(event.pos):
                        Color4 = NewColor
                    else:
                        Color1 = Color2 = Color3 = Color4 = DefaultColor
                if event.type == MOUSEBUTTONDOWN:
                    if settingButton.collidepoint(event.pos):
                        colorSetting()
                    if BackButton.collidepoint(event.pos):
                        return
                    if NextStepButton.collidepoint(event.pos):

                        numberOfRings = NumberChosen
                        if RingPuzzleSet9[0] == 0 and RingPuzzleSet9[1] == 0 and RingPuzzleSet9[2] == 0 and \
                                RingPuzzleSet9[3] == 0 and RingPuzzleSet9[4] == 0 and RingPuzzleSet9[5] == 0 and \
                                RingPuzzleSet9[6] == 0 and RingPuzzleSet9[7] == 0 and RingPuzzleSet9[8] == 0:
                            RingPuzzleSet9[0] = 0
                            yCord1 = offY
                        else:
                            j = int(j) + 1
                            x = [int(a) for a in str(solveRings(NumberChosen)[j - 1])]
                            for k in range(NumberChosen):
                                numberOfRings = numberOfRings - 1
                                newX = x[k]
                                if newX == 0:
                                    RingPuzzleSet9[numberOfRings] = 0
                                if newX == 1:
                                    RingPuzzleSet9[numberOfRings] = 1
                                if RingPuzzleSet9[0] == 0:
                                    yCord1 = offY
                                if RingPuzzleSet9[0] == 1:
                                    yCord1 = onY
                                if RingPuzzleSet9[1] == 0:
                                    yCord2 = offY
                                if RingPuzzleSet9[1] == 1:
                                    yCord2 = onY
                                if RingPuzzleSet9[2] == 0:
                                    yCord3 = offY
                                if RingPuzzleSet9[2] == 1:
                                    yCord3 = onY
                                if RingPuzzleSet9[3] == 0:
                                    yCord4 = offY
                                if RingPuzzleSet9[3] == 1:
                                    yCord4 = onY
                                if RingPuzzleSet9[4] == 0:
                                    yCord5 = offY
                                if RingPuzzleSet9[4] == 1:
                                    yCord5 = onY
                                if RingPuzzleSet9[5] == 0:
                                    yCord6 = offY
                                if RingPuzzleSet9[5] == 1:
                                    yCord6 = onY
                                if RingPuzzleSet9[6] == 0:
                                    yCord7 = offY
                                if RingPuzzleSet9[6] == 1:
                                    yCord7 = onY
                                if RingPuzzleSet9[7] == 0:
                                    yCord8 = offY
                                if RingPuzzleSet9[7] == 1:
                                    yCord8 = onY
                                if RingPuzzleSet9[8] == 0:
                                    yCord9 = offY
                                if RingPuzzleSet9[8] == 1:
                                    yCord9 = onY

        if NumberChosen == 2:
            pygame.draw.rect(WINDOWSURFACE, backgroundColor, firstRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[0]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (firstRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=firstRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, secondRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[1]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (secondRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=secondRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            for event in pygame.event.get():
                checkTermination(event)
                if event.type == MOUSEMOTION:
                    if BackButton.collidepoint(event.pos):
                        Color2 = NewColor
                    elif settingButton.collidepoint(event.pos):
                        Color3 = NewColor
                    elif NextStepButton.collidepoint(event.pos):
                        Color4 = NewColor
                    else:
                        Color1 = Color2 = Color3 = Color4 = DefaultColor
                if event.type == MOUSEBUTTONDOWN:
                    if settingButton.collidepoint(event.pos):
                        colorSetting()
                    if BackButton.collidepoint(event.pos):
                        return
                    if NextStepButton.collidepoint(event.pos):

                        numberOfRings = NumberChosen
                        if RingPuzzleSet9[0] == 0 and RingPuzzleSet9[1] == 0 and RingPuzzleSet9[2] == 0 and \
                                RingPuzzleSet9[3] == 0 and RingPuzzleSet9[4] == 0 and RingPuzzleSet9[5] == 0 and \
                                RingPuzzleSet9[6] == 0 and RingPuzzleSet9[7] == 0 and RingPuzzleSet9[8] == 0:
                            RingPuzzleSet9[0] = 0
                            yCord1 = offY
                        else:
                            j = int(j) + 1
                            x = [int(a) for a in str(solveRings(NumberChosen)[j - 1])]
                            for k in range(NumberChosen):
                                numberOfRings = numberOfRings - 1
                                newX = x[k]
                                if newX == 0:
                                    RingPuzzleSet9[numberOfRings] = 0
                                if newX == 1:
                                    RingPuzzleSet9[numberOfRings] = 1
                                if RingPuzzleSet9[0] == 0:
                                    yCord1 = offY
                                if RingPuzzleSet9[0] == 1:
                                    yCord1 = onY
                                if RingPuzzleSet9[1] == 0:
                                    yCord2 = offY
                                if RingPuzzleSet9[1] == 1:
                                    yCord2 = onY
                                if RingPuzzleSet9[2] == 0:
                                    yCord3 = offY
                                if RingPuzzleSet9[2] == 1:
                                    yCord3 = onY
                                if RingPuzzleSet9[3] == 0:
                                    yCord4 = offY
                                if RingPuzzleSet9[3] == 1:
                                    yCord4 = onY
                                if RingPuzzleSet9[4] == 0:
                                    yCord5 = offY
                                if RingPuzzleSet9[4] == 1:
                                    yCord5 = onY
                                if RingPuzzleSet9[5] == 0:
                                    yCord6 = offY
                                if RingPuzzleSet9[5] == 1:
                                    yCord6 = onY
                                if RingPuzzleSet9[6] == 0:
                                    yCord7 = offY
                                if RingPuzzleSet9[6] == 1:
                                    yCord7 = onY
                                if RingPuzzleSet9[7] == 0:
                                    yCord8 = offY
                                if RingPuzzleSet9[7] == 1:
                                    yCord8 = onY
                                if RingPuzzleSet9[8] == 0:
                                    yCord9 = offY
                                if RingPuzzleSet9[8] == 1:
                                    yCord9 = onY

        if NumberChosen == 3:
            pygame.draw.rect(WINDOWSURFACE, backgroundColor, firstRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[0]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (firstRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=firstRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, secondRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[1]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (secondRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=secondRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, thirdRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[2]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (thirdRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=thirdRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            for event in pygame.event.get():
                checkTermination(event)
                if event.type == MOUSEMOTION:
                    if BackButton.collidepoint(event.pos):
                        Color2 = NewColor
                    elif settingButton.collidepoint(event.pos):
                        Color3 = NewColor
                    elif NextStepButton.collidepoint(event.pos):
                        Color4 = NewColor
                    else:
                        Color1 = Color2 = Color3 = Color4 = DefaultColor
                if event.type == MOUSEBUTTONDOWN:
                    if settingButton.collidepoint(event.pos):
                        colorSetting()
                    if BackButton.collidepoint(event.pos):
                        return
                    if NextStepButton.collidepoint(event.pos):

                        numberOfRings = NumberChosen
                        if RingPuzzleSet9[0] == 0 and RingPuzzleSet9[1] == 0 and RingPuzzleSet9[2] == 0 and \
                                RingPuzzleSet9[3] == 0 and RingPuzzleSet9[4] == 0 and RingPuzzleSet9[5] == 0 and \
                                RingPuzzleSet9[6] == 0 and RingPuzzleSet9[7] == 0 and RingPuzzleSet9[8] == 0:
                            RingPuzzleSet9[0] = 0
                            yCord1 = offY
                        else:
                            j = int(j) + 1
                            x = [int(a) for a in str(solveRings(NumberChosen)[j - 1])]
                            for k in range(NumberChosen):
                                numberOfRings = numberOfRings - 1
                                newX = x[k]
                                if newX == 0:
                                    RingPuzzleSet9[numberOfRings] = 0
                                if newX == 1:
                                    RingPuzzleSet9[numberOfRings] = 1
                                if RingPuzzleSet9[0] == 0:
                                    yCord1 = offY
                                if RingPuzzleSet9[0] == 1:
                                    yCord1 = onY
                                if RingPuzzleSet9[1] == 0:
                                    yCord2 = offY
                                if RingPuzzleSet9[1] == 1:
                                    yCord2 = onY
                                if RingPuzzleSet9[2] == 0:
                                    yCord3 = offY
                                if RingPuzzleSet9[2] == 1:
                                    yCord3 = onY
                                if RingPuzzleSet9[3] == 0:
                                    yCord4 = offY
                                if RingPuzzleSet9[3] == 1:
                                    yCord4 = onY
                                if RingPuzzleSet9[4] == 0:
                                    yCord5 = offY
                                if RingPuzzleSet9[4] == 1:
                                    yCord5 = onY
                                if RingPuzzleSet9[5] == 0:
                                    yCord6 = offY
                                if RingPuzzleSet9[5] == 1:
                                    yCord6 = onY
                                if RingPuzzleSet9[6] == 0:
                                    yCord7 = offY
                                if RingPuzzleSet9[6] == 1:
                                    yCord7 = onY
                                if RingPuzzleSet9[7] == 0:
                                    yCord8 = offY
                                if RingPuzzleSet9[7] == 1:
                                    yCord8 = onY
                                if RingPuzzleSet9[8] == 0:
                                    yCord9 = offY
                                if RingPuzzleSet9[8] == 1:
                                    yCord9 = onY

        if NumberChosen == 4:
            pygame.draw.rect(WINDOWSURFACE, backgroundColor, firstRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[0]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (firstRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=firstRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, secondRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[1]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (secondRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=secondRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, thirdRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[2]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (thirdRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=thirdRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, fourthRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[3]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (fourthRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=fourthRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            for event in pygame.event.get():
                checkTermination(event)
                if event.type == MOUSEMOTION:
                    if BackButton.collidepoint(event.pos):
                        Color2 = NewColor
                    elif settingButton.collidepoint(event.pos):
                        Color3 = NewColor
                    elif NextStepButton.collidepoint(event.pos):
                        Color4 = NewColor
                    else:
                        Color1 = Color2 = Color3 = Color4 = DefaultColor
                if event.type == MOUSEBUTTONDOWN:
                    if settingButton.collidepoint(event.pos):
                        colorSetting()
                    if BackButton.collidepoint(event.pos):
                        return
                    if NextStepButton.collidepoint(event.pos):

                        numberOfRings = NumberChosen
                        if RingPuzzleSet9[0] == 0 and RingPuzzleSet9[1] == 0 and RingPuzzleSet9[2] == 0 and \
                                RingPuzzleSet9[3] == 0 and RingPuzzleSet9[4] == 0 and RingPuzzleSet9[5] == 0 and \
                                RingPuzzleSet9[6] == 0 and RingPuzzleSet9[7] == 0 and RingPuzzleSet9[8] == 0:
                            RingPuzzleSet9[0] = 0
                            yCord1 = offY
                        else:
                            j = int(j) + 1
                            x = [int(a) for a in str(solveRings(NumberChosen)[j - 1])]
                            for k in range(NumberChosen):
                                numberOfRings = numberOfRings - 1
                                newX = x[k]
                                if newX == 0:
                                    RingPuzzleSet9[numberOfRings] = 0
                                if newX == 1:
                                    RingPuzzleSet9[numberOfRings] = 1
                                if RingPuzzleSet9[0] == 0:
                                    yCord1 = offY
                                if RingPuzzleSet9[0] == 1:
                                    yCord1 = onY
                                if RingPuzzleSet9[1] == 0:
                                    yCord2 = offY
                                if RingPuzzleSet9[1] == 1:
                                    yCord2 = onY
                                if RingPuzzleSet9[2] == 0:
                                    yCord3 = offY
                                if RingPuzzleSet9[2] == 1:
                                    yCord3 = onY
                                if RingPuzzleSet9[3] == 0:
                                    yCord4 = offY
                                if RingPuzzleSet9[3] == 1:
                                    yCord4 = onY
                                if RingPuzzleSet9[4] == 0:
                                    yCord5 = offY
                                if RingPuzzleSet9[4] == 1:
                                    yCord5 = onY
                                if RingPuzzleSet9[5] == 0:
                                    yCord6 = offY
                                if RingPuzzleSet9[5] == 1:
                                    yCord6 = onY
                                if RingPuzzleSet9[6] == 0:
                                    yCord7 = offY
                                if RingPuzzleSet9[6] == 1:
                                    yCord7 = onY
                                if RingPuzzleSet9[7] == 0:
                                    yCord8 = offY
                                if RingPuzzleSet9[7] == 1:
                                    yCord8 = onY
                                if RingPuzzleSet9[8] == 0:
                                    yCord9 = offY
                                if RingPuzzleSet9[8] == 1:
                                    yCord9 = onY

        if NumberChosen == 5:
            pygame.draw.rect(WINDOWSURFACE, backgroundColor, firstRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[0]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (firstRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=firstRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, secondRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[1]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (secondRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=secondRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, thirdRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[2]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (thirdRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=thirdRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, fourthRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[3]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (fourthRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=fourthRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, fifthRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[4]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (fifthRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=fifthRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            for event in pygame.event.get():
                checkTermination(event)
                if event.type == MOUSEMOTION:
                    if BackButton.collidepoint(event.pos):
                        Color2 = NewColor
                    elif settingButton.collidepoint(event.pos):
                        Color3 = NewColor
                    elif NextStepButton.collidepoint(event.pos):
                        Color4 = NewColor
                    else:
                        Color1 = Color2 = Color3 = Color4 = DefaultColor
                if event.type == MOUSEBUTTONDOWN:
                    if settingButton.collidepoint(event.pos):
                        colorSetting()
                    if BackButton.collidepoint(event.pos):
                        return
                    if NextStepButton.collidepoint(event.pos):

                        numberOfRings = NumberChosen
                        if RingPuzzleSet9[0] == 0 and RingPuzzleSet9[1] == 0 and RingPuzzleSet9[2] == 0 and \
                                RingPuzzleSet9[3] == 0 and RingPuzzleSet9[4] == 0 and RingPuzzleSet9[5] == 0 and \
                                RingPuzzleSet9[6] == 0 and RingPuzzleSet9[7] == 0 and RingPuzzleSet9[8] == 0:
                            RingPuzzleSet9[0] = 0
                            yCord1 = offY
                        else:
                            j = int(j) + 1
                            x = [int(a) for a in str(solveRings(NumberChosen)[j - 1])]
                            for k in range(NumberChosen):
                                numberOfRings = numberOfRings - 1
                                newX = x[k]
                                if newX == 0:
                                    RingPuzzleSet9[numberOfRings] = 0
                                if newX == 1:
                                    RingPuzzleSet9[numberOfRings] = 1
                                if RingPuzzleSet9[0] == 0:
                                    yCord1 = offY
                                if RingPuzzleSet9[0] == 1:
                                    yCord1 = onY
                                if RingPuzzleSet9[1] == 0:
                                    yCord2 = offY
                                if RingPuzzleSet9[1] == 1:
                                    yCord2 = onY
                                if RingPuzzleSet9[2] == 0:
                                    yCord3 = offY
                                if RingPuzzleSet9[2] == 1:
                                    yCord3 = onY
                                if RingPuzzleSet9[3] == 0:
                                    yCord4 = offY
                                if RingPuzzleSet9[3] == 1:
                                    yCord4 = onY
                                if RingPuzzleSet9[4] == 0:
                                    yCord5 = offY
                                if RingPuzzleSet9[4] == 1:
                                    yCord5 = onY
                                if RingPuzzleSet9[5] == 0:
                                    yCord6 = offY
                                if RingPuzzleSet9[5] == 1:
                                    yCord6 = onY
                                if RingPuzzleSet9[6] == 0:
                                    yCord7 = offY
                                if RingPuzzleSet9[6] == 1:
                                    yCord7 = onY
                                if RingPuzzleSet9[7] == 0:
                                    yCord8 = offY
                                if RingPuzzleSet9[7] == 1:
                                    yCord8 = onY
                                if RingPuzzleSet9[8] == 0:
                                    yCord9 = offY
                                if RingPuzzleSet9[8] == 1:
                                    yCord9 = onY

        if NumberChosen == 6:
            pygame.draw.rect(WINDOWSURFACE, backgroundColor, firstRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[0]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (firstRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=firstRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, secondRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[1]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (secondRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=secondRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, thirdRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[2]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (thirdRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=thirdRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, fourthRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[3]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (fourthRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=fourthRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, fifthRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[4]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (fifthRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=fifthRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, sixthRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[5]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (sixthRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=sixthRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            for event in pygame.event.get():
                checkTermination(event)
                if event.type == MOUSEMOTION:
                    if BackButton.collidepoint(event.pos):
                        Color2 = NewColor
                    elif settingButton.collidepoint(event.pos):
                        Color3 = NewColor
                    elif NextStepButton.collidepoint(event.pos):
                        Color4 = NewColor
                    else:
                        Color1 = Color2 = Color3 = Color4 = DefaultColor
                if event.type == MOUSEBUTTONDOWN:
                    if settingButton.collidepoint(event.pos):
                        colorSetting()
                    if BackButton.collidepoint(event.pos):
                        return
                    if NextStepButton.collidepoint(event.pos):

                        numberOfRings = NumberChosen
                        if RingPuzzleSet9[0] == 0 and RingPuzzleSet9[1] == 0 and RingPuzzleSet9[2] == 0 and \
                                RingPuzzleSet9[3] == 0 and RingPuzzleSet9[4] == 0 and RingPuzzleSet9[5] == 0 and \
                                RingPuzzleSet9[6] == 0 and RingPuzzleSet9[7] == 0 and RingPuzzleSet9[8] == 0:
                            RingPuzzleSet9[0] = 0
                            yCord1 = offY
                        else:
                            j = int(j) + 1
                            x = [int(a) for a in str(solveRings(NumberChosen)[j - 1])]
                            for k in range(NumberChosen):
                                numberOfRings = numberOfRings - 1
                                newX = x[k]
                                if newX == 0:
                                    RingPuzzleSet9[numberOfRings] = 0
                                if newX == 1:
                                    RingPuzzleSet9[numberOfRings] = 1
                                if RingPuzzleSet9[0] == 0:
                                    yCord1 = offY
                                if RingPuzzleSet9[0] == 1:
                                    yCord1 = onY
                                if RingPuzzleSet9[1] == 0:
                                    yCord2 = offY
                                if RingPuzzleSet9[1] == 1:
                                    yCord2 = onY
                                if RingPuzzleSet9[2] == 0:
                                    yCord3 = offY
                                if RingPuzzleSet9[2] == 1:
                                    yCord3 = onY
                                if RingPuzzleSet9[3] == 0:
                                    yCord4 = offY
                                if RingPuzzleSet9[3] == 1:
                                    yCord4 = onY
                                if RingPuzzleSet9[4] == 0:
                                    yCord5 = offY
                                if RingPuzzleSet9[4] == 1:
                                    yCord5 = onY
                                if RingPuzzleSet9[5] == 0:
                                    yCord6 = offY
                                if RingPuzzleSet9[5] == 1:
                                    yCord6 = onY
                                if RingPuzzleSet9[6] == 0:
                                    yCord7 = offY
                                if RingPuzzleSet9[6] == 1:
                                    yCord7 = onY
                                if RingPuzzleSet9[7] == 0:
                                    yCord8 = offY
                                if RingPuzzleSet9[7] == 1:
                                    yCord8 = onY
                                if RingPuzzleSet9[8] == 0:
                                    yCord9 = offY
                                if RingPuzzleSet9[8] == 1:
                                    yCord9 = onY

        if NumberChosen == 7:
            pygame.draw.rect(WINDOWSURFACE, backgroundColor, firstRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[0]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (firstRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=firstRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, secondRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[1]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (secondRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=secondRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, thirdRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[2]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (thirdRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=thirdRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, fourthRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[3]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (fourthRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=fourthRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, fifthRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[4]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (fifthRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=fifthRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, sixthRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[5]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (sixthRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=sixthRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, seventhRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[6]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (seventhRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=seventhRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            for event in pygame.event.get():
                checkTermination(event)
                if event.type == MOUSEMOTION:
                    if BackButton.collidepoint(event.pos):
                        Color2 = NewColor
                    elif settingButton.collidepoint(event.pos):
                        Color3 = NewColor
                    elif NextStepButton.collidepoint(event.pos):
                        Color4 = NewColor
                    else:
                        Color1 = Color2 = Color3 = Color4 = DefaultColor
                if event.type == MOUSEBUTTONDOWN:
                    if settingButton.collidepoint(event.pos):
                        colorSetting()
                    if BackButton.collidepoint(event.pos):
                        return
                    if NextStepButton.collidepoint(event.pos):

                        numberOfRings = NumberChosen
                        if RingPuzzleSet9[0] == 0 and RingPuzzleSet9[1] == 0 and RingPuzzleSet9[2] == 0 and \
                                RingPuzzleSet9[3] == 0 and RingPuzzleSet9[4] == 0 and RingPuzzleSet9[5] == 0 and \
                                RingPuzzleSet9[6] == 0 and RingPuzzleSet9[7] == 0 and RingPuzzleSet9[8] == 0:
                            RingPuzzleSet9[0] = 0
                            yCord1 = offY
                        else:
                            j = int(j) + 1
                            x = [int(a) for a in str(solveRings(NumberChosen)[j - 1])]
                            for k in range(NumberChosen):
                                numberOfRings = numberOfRings - 1
                                newX = x[k]
                                if newX == 0:
                                    RingPuzzleSet9[numberOfRings] = 0
                                if newX == 1:
                                    RingPuzzleSet9[numberOfRings] = 1
                                if RingPuzzleSet9[0] == 0:
                                    yCord1 = offY
                                if RingPuzzleSet9[0] == 1:
                                    yCord1 = onY
                                if RingPuzzleSet9[1] == 0:
                                    yCord2 = offY
                                if RingPuzzleSet9[1] == 1:
                                    yCord2 = onY
                                if RingPuzzleSet9[2] == 0:
                                    yCord3 = offY
                                if RingPuzzleSet9[2] == 1:
                                    yCord3 = onY
                                if RingPuzzleSet9[3] == 0:
                                    yCord4 = offY
                                if RingPuzzleSet9[3] == 1:
                                    yCord4 = onY
                                if RingPuzzleSet9[4] == 0:
                                    yCord5 = offY
                                if RingPuzzleSet9[4] == 1:
                                    yCord5 = onY
                                if RingPuzzleSet9[5] == 0:
                                    yCord6 = offY
                                if RingPuzzleSet9[5] == 1:
                                    yCord6 = onY
                                if RingPuzzleSet9[6] == 0:
                                    yCord7 = offY
                                if RingPuzzleSet9[6] == 1:
                                    yCord7 = onY
                                if RingPuzzleSet9[7] == 0:
                                    yCord8 = offY
                                if RingPuzzleSet9[7] == 1:
                                    yCord8 = onY
                                if RingPuzzleSet9[8] == 0:
                                    yCord9 = offY
                                if RingPuzzleSet9[8] == 1:
                                    yCord9 = onY

        if NumberChosen == 8:
            pygame.draw.rect(WINDOWSURFACE, backgroundColor, firstRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[0]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (firstRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=firstRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, secondRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[1]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (secondRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=secondRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, thirdRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[2]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (thirdRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=thirdRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, fourthRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[3]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (fourthRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=fourthRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, fifthRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[4]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (fifthRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=fifthRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, sixthRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[5]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (sixthRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=sixthRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, seventhRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[6]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (seventhRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=seventhRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, eighthRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[7]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (eighthRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=eighthRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            for event in pygame.event.get():
                checkTermination(event)
                if event.type == MOUSEMOTION:
                    if BackButton.collidepoint(event.pos):
                        Color2 = NewColor
                    elif settingButton.collidepoint(event.pos):
                        Color3 = NewColor
                    elif NextStepButton.collidepoint(event.pos):
                        Color4 = NewColor
                    else:
                        Color1 = Color2 = Color3 = Color4 = DefaultColor
                if event.type == MOUSEBUTTONDOWN:
                    if settingButton.collidepoint(event.pos):
                        colorSetting()
                    if BackButton.collidepoint(event.pos):
                        return
                    if NextStepButton.collidepoint(event.pos):

                        numberOfRings = NumberChosen
                        if RingPuzzleSet9[0] == 0 and RingPuzzleSet9[1] == 0 and RingPuzzleSet9[2] == 0 and \
                                RingPuzzleSet9[3] == 0 and RingPuzzleSet9[4] == 0 and RingPuzzleSet9[5] == 0 and \
                                RingPuzzleSet9[6] == 0 and RingPuzzleSet9[7] == 0 and RingPuzzleSet9[8] == 0:
                            RingPuzzleSet9[0] = 0
                            yCord1 = offY
                        else:
                            j = int(j) + 1
                            x = [int(a) for a in str(solveRings(NumberChosen)[j - 1])]
                            for k in range(NumberChosen):
                                numberOfRings = numberOfRings - 1
                                newX = x[k]
                                if newX == 0:
                                    RingPuzzleSet9[numberOfRings] = 0
                                if newX == 1:
                                    RingPuzzleSet9[numberOfRings] = 1
                                if RingPuzzleSet9[0] == 0:
                                    yCord1 = offY
                                if RingPuzzleSet9[0] == 1:
                                    yCord1 = onY
                                if RingPuzzleSet9[1] == 0:
                                    yCord2 = offY
                                if RingPuzzleSet9[1] == 1:
                                    yCord2 = onY
                                if RingPuzzleSet9[2] == 0:
                                    yCord3 = offY
                                if RingPuzzleSet9[2] == 1:
                                    yCord3 = onY
                                if RingPuzzleSet9[3] == 0:
                                    yCord4 = offY
                                if RingPuzzleSet9[3] == 1:
                                    yCord4 = onY
                                if RingPuzzleSet9[4] == 0:
                                    yCord5 = offY
                                if RingPuzzleSet9[4] == 1:
                                    yCord5 = onY
                                if RingPuzzleSet9[5] == 0:
                                    yCord6 = offY
                                if RingPuzzleSet9[5] == 1:
                                    yCord6 = onY
                                if RingPuzzleSet9[6] == 0:
                                    yCord7 = offY
                                if RingPuzzleSet9[6] == 1:
                                    yCord7 = onY
                                if RingPuzzleSet9[7] == 0:
                                    yCord8 = offY
                                if RingPuzzleSet9[7] == 1:
                                    yCord8 = onY
                                if RingPuzzleSet9[8] == 0:
                                    yCord9 = offY
                                if RingPuzzleSet9[8] == 1:
                                    yCord9 = onY

        if NumberChosen == 9:
            pygame.draw.rect(WINDOWSURFACE, backgroundColor, firstRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[0]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (firstRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=firstRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, secondRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[1]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (secondRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=secondRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, thirdRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[2]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (thirdRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=thirdRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, fourthRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[3]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (fourthRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=fourthRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, fifthRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[4]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (fifthRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=fifthRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, sixthRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[5]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (sixthRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=sixthRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, seventhRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[6]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (seventhRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=seventhRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, eighthRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[7]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (eighthRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=eighthRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            pygame.draw.rect(WINDOWSURFACE, backgroundColor, ninthRingNumber)
            NextStepChoiceText = bigFont.render(str(RingPuzzleSet9[8]), True, textColor, backgroundColor)
            NextStepTextRectangle = NextStepChoiceText.get_rect()
            NextStepTextRectangle.center = (ninthRingNumber.center)
            NextStepChoiceTextRect = NextStepChoiceText.get_rect(center=ninthRingNumber.center)
            WINDOWSURFACE.blit(NextStepChoiceText, NextStepChoiceTextRect)

            for event in pygame.event.get():
                checkTermination(event)
                if event.type == MOUSEMOTION:
                    if BackButton.collidepoint(event.pos):
                        Color2 = NewColor
                    elif settingButton.collidepoint(event.pos):
                        Color3 = NewColor
                    elif NextStepButton.collidepoint(event.pos):
                        Color4 = NewColor
                    else:
                        Color1 = Color2 = Color3 = Color4 = DefaultColor
                if event.type == MOUSEBUTTONDOWN:
                    if settingButton.collidepoint(event.pos):
                        colorSetting()
                    if BackButton.collidepoint(event.pos):
                        return
                    if NextStepButton.collidepoint(event.pos):

                        numberOfRings = NumberChosen
                        if RingPuzzleSet9[0] == 0 and RingPuzzleSet9[1] == 0 and RingPuzzleSet9[2] == 0 and \
                                RingPuzzleSet9[3] == 0 and RingPuzzleSet9[4] == 0 and RingPuzzleSet9[5] == 0 and \
                                RingPuzzleSet9[6] == 0 and RingPuzzleSet9[7] == 0 and RingPuzzleSet9[8] == 0:
                            RingPuzzleSet9[0] = 0
                            yCord1 = offY
                        else:
                            j = int(j) + 1
                            x = [int(a) for a in str(solveRings(NumberChosen)[j - 1])]
                            for k in range(NumberChosen):
                                numberOfRings = numberOfRings - 1
                                newX = x[k]
                                if newX == 0:
                                    RingPuzzleSet9[numberOfRings] = 0
                                if newX == 1:
                                    RingPuzzleSet9[numberOfRings] = 1
                                if RingPuzzleSet9[0] == 0:
                                    yCord1 = offY
                                if RingPuzzleSet9[0] == 1:
                                    yCord1 = onY
                                if RingPuzzleSet9[1] == 0:
                                    yCord2 = offY
                                if RingPuzzleSet9[1] == 1:
                                    yCord2 = onY
                                if RingPuzzleSet9[2] == 0:
                                    yCord3 = offY
                                if RingPuzzleSet9[2] == 1:
                                    yCord3 = onY
                                if RingPuzzleSet9[3] == 0:
                                    yCord4 = offY
                                if RingPuzzleSet9[3] == 1:
                                    yCord4 = onY
                                if RingPuzzleSet9[4] == 0:
                                    yCord5 = offY
                                if RingPuzzleSet9[4] == 1:
                                    yCord5 = onY
                                if RingPuzzleSet9[5] == 0:
                                    yCord6 = offY
                                if RingPuzzleSet9[5] == 1:
                                    yCord6 = onY
                                if RingPuzzleSet9[6] == 0:
                                    yCord7 = offY
                                if RingPuzzleSet9[6] == 1:
                                    yCord7 = onY
                                if RingPuzzleSet9[7] == 0:
                                    yCord8 = offY
                                if RingPuzzleSet9[7] == 1:
                                    yCord8 = onY
                                if RingPuzzleSet9[8] == 0:
                                    yCord9 = offY
                                if RingPuzzleSet9[8] == 1:
                                    yCord9 = onY


        RefreshScreen()


IntroductionScreen()

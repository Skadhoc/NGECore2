import sys
 
def addHyperPoints(core, planet):

	if planet.getName() == 'space_corellia':
        space_corelliaHyperPoints(core, planet)
    if planet.getName() == 'space_dantooine':
        space_dantooineHyperPoints(core, planet)
    if planet.getName() == 'space_dathomir':
        space_dathomirHyperPoints(core, planet)
    if planet.getName() == 'space_endor':
        space_endorHyperPoints(core, planet)
    if planet.getName() == 'space_lok':
        space_lokHyperPoints(core, planet)
    if planet.getName() == 'space_naboo':
        space_nabooHyperPoints(core, planet)
    if planet.getName() == 'nova_orion':
        nova_orionHyperPoints(core, planet)
    if planet.getName() == 'space_tatooine':
        space_tatooineHyperPoints(core, planet)
    if planet.getName() == 'space_yavin4':
        space_yavin4HyperPoints(core, planet)    
    if planet.getName() == 'space_kashyyyk':
    	space_kashyyykHyperPoints(core, planet)  
    return
    
def space_corelliaPoints(core, planet):
    trvSvc = core.travelService
   
    trvSvc.addTravelPoint(planet, "Corsec Wing", -967, -1188, 0)
    trvSvc.addTravelPoint(planet, "Trifecta Star", -4962, 4029, 3442)
    trvSvc.addTravelPoint(planet, "Binayre Razorcat", 1840, 2981, 944)
    trvSvc.addTravelPoint(planet, "Corellia's Own", 6981, -3252, -5997)
    trvSvc.addTravelPoint(planet, "Talus Secta", -3778, -1807, -1689)
    return        

def space_dantooinePoints(core, planet):
    trvSvc = core.travelService
   
    trvSvc.addTravelPoint(planet, "Dantooine's Wrath", -1454, -1065, 246)
    trvSvc.addTravelPoint(planet, "Asair's Ribbon", -6334, -3411, 2155)
    trvSvc.addTravelPoint(planet, "Isryn's Veil", 6633, -5131, -1009)
    trvSvc.addTravelPoint(planet, "Gorvera Space", -6411, 6756, 6426)
    return                
        
def space_dathomirPoints(core, planet):
    trvSvc = core.travelService
   
    trvSvc.addTravelPoint(planet, "Dark Force", 869, -49, 2392)
    trvSvc.addTravelPoint(planet, "Empire Blockade", 3825, 1983, 2612)
    trvSvc.addTravelPoint(planet, "Dathomir's Vitality", -1256, -2660, -5971)
    trvSvc.addTravelPoint(planet, "Emperor's Hand", -6728, -1956, 5916)
    return        

def space_endorPoints(core, planet):
    trvSvc = core.travelService
   
    trvSvc.addTravelPoint(planet, "Red Sin Chimera", 639, -3624, -4638)
    trvSvc.addTravelPoint(planet, "Area D-435", -1965, 2651, 3708)
    trvSvc.addTravelPoint(planet, "Empire's Justice", -6929, 4251, -1973)
    trvSvc.addTravelPoint(planet, "Durillium Sea", 5737, 2601, 3735)
    return        
        
def space_lokPoints(core, planet):
    trvSvc = core.travelService
   
    trvSvc.addTravelPoint(planet, "Nym's Hovel", -505, 4746, 4459)
    trvSvc.addTravelPoint(planet, "Rebellion Blaze", 1499, -5126, -5962)
    trvSvc.addTravelPoint(planet, "Lurid Dawn", -6926, -172, 955)
    trvSvc.addTravelPoint(planet, "Voria's Ember", 6492, 1803, -524)
    return

def space_nabooPoints(core, planet):
    trvSvc = core.travelService
   
    trvSvc.addTravelPoint(planet, "Royal Way", -944, 4270, -4525)
    trvSvc.addTravelPoint(planet, "Penumbra Omen", -2992, 4309, 3520)
    trvSvc.addTravelPoint(planet, "Sea of Veruna", 5935, -657, 2946)
    trvSvc.addTravelPoint(planet, "Kylantha's Whim", -5952, -2433, -5005)
    return        
        
def nova_orionPoints(core, planet):
    trvSvc = core.travelService
   
    trvSvc.addTravelPoint(planet, "nova_orion_entrance", -890, 485, -305)
    return                
        
def space_tatooinePoints(core, planet):
    trvSvc = core.travelService
   
    trvSvc.addTravelPoint(planet, "Deap Sea", -4933, 6764, 6890)
    trvSvc.addTravelPoint(planet, "Miner's Yard", 5475, 4780, 6433)
    trvSvc.addTravelPoint(planet, "Desert Sands", 6451, -1203, -3502)
    trvSvc.addTravelPoint(planet, "Outer Rim", -6933, -3187, 970)
    return
        
def space_yavin4Points(core, planet):
    trvSvc = core.travelService
   
    trvSvc.addTravelPoint(planet, "0", -962, 4805, 6923)
    trvSvc.addTravelPoint(planet, "1", 4988, -5654, -6482)
    trvSvc.addTravelPoint(planet, "2", -960, -2174, -6143)
    return
    
def space_kashyyykPoints(core, planet):
    trvSvc = core.travelService
   
    trvSvc.addTravelPoint(planet, "Neutral Territories", -3000, 250, -3000)
    trvSvc.addTravelPoint(planet, "Avatar Platform", 1000, 600, -1000)
    trvSvc.addTravelPoint(planet, "Imperial Overseer's Base", 5000, 1200, -5800)
    trvSvc.addTravelPoint(planet, "Rodian Territories", -2000, 250, 3500)
    return   
    
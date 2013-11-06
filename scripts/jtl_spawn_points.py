import sys
 
def addJTLSpawnPoints(core, planet):

	if planet.getName() == 'space_corellia':
        space_corelliaJTLSpawnPoints(core, planet)
    if planet.getName() == 'space_dantooine':
        space_dantooineJTLSpawnPoints(core, planet)
    if planet.getName() == 'space_dathomir':
        space_dathomirJTLSpawnPoints(core, planet)
    if planet.getName() == 'space_endor':
        space_endorJTLSpawnPoints(core, planet)
    if planet.getName() == 'space_lok':
        space_lokJTLSpawnPoints(core, planet)
    if planet.getName() == 'space_naboo':
        space_nabooJTLSpawnPoints(core, planet)
    if planet.getName() == 'nova_orion':
        nova_orionJTLSpawnPoints(core, planet)
    if planet.getName() == 'space_tatooine':
        space_tatooineJTLSpawnPoints(core, planet)
    if planet.getName() == 'space_yavin4':
        space_yavin4JTLSpawnPoints(core, planet)    
    if planet.getName() == 'space_kashyyyk':
    	space_kashyyykJTLSpawnPoints(core, planet)
    if planet.getName() == 'ord_mantell':
    	ord_mantellJTLSpawnPoints(core, planet)
    if planet.getName() == 'deep_space':
    	deep_spaceJTLSpawnPoints(core, planet)
    if planet.getName() == 'kessel':
    	kesselJTLSpawnPoints(core, planet)  
    return
    
def space_corelliaJTLSpawnPoints(core, planet):
    trvSvc = core.travelService
   
    trvSvc.addJTLSpawnPoint(planet, "Corellia Launch", , , )
    trvSvc.addJTLSpawnPoint(planet, "Talus Launch", , , )
    return        

def space_dantooinePoints(core, planet):
    trvSvc = core.travelService
   
    trvSvc.addJTLSpawnPoint(planet, "Dantooine Launch", , , )
    return                
        
def space_dathomirPoints(core, planet):
    trvSvc = core.travelService
   
    trvSvc.addJTLSpawnPoint(planet, "Dathomir Launch", , , )
    return        

def space_endorPoints(core, planet):
    trvSvc = core.travelService
   
   trvSvc.addJTLSpawnPoint(planet, "Endor Launch", , , )
    return        
        
def space_lokPoints(core, planet):
    trvSvc = core.travelService
   
   trvSvc.addJTLSpawnPoint(planet, "Lok Launch", , , )
    return

def space_nabooPoints(core, planet):
    trvSvc = core.travelService
   
    trvSvc.addJTLSpawnPoint(planet, "Naboo Launch", , , )
    trvSvc.addJTLSpawnPoint(planet, "Rori Launch", , , )
    return        
        
def nova_orionPoints(core, planet):
    trvSvc = core.travelService
   
    trvSvc.addTravelPoint(planet, "nova_orion Entrance", -890, 485, -305)
    return                
        
def space_tatooinePoints(core, planet):
    trvSvc = core.travelService
   
   trvSvc.addJTLSpawnPoint(planet, "Tatooine Launch", , , )
    return
        
def space_yavin4Points(core, planet):
    trvSvc = core.travelService
   
    trvSvc.addJTLSpawnPoint(planet, "Yavin4 Launch", , , )
    return
    
def space_kashyyykPoints(core, planet):
    trvSvc = core.travelService
   
     trvSvc.addJTLSpawnPoint(planet, "Kashyyyk Launch", , , )
     trvSvc.addJTLSpawnPoint(planet, "Avatar Launch", , , )
    return 
    
def ord_mantellJTLSpawnPoints(core, planet):
    trvSvc = core.travelService
   
     trvSvc.addJTLSpawnPoint(planet, "Tansarii launch", 67, -35, 33)
     trvSvc.addJTLSpawnPoint(planet, "Gamma Launch", 539, -725, 1497)
    return 
    
def deep_spaceJTLSpawnPoints(core, planet):
    trvSvc = core.travelService
   
     trvSvc.addJTLSpawnPoint(planet, "Imperial Entrance", , , )
     trvSvc.addJTLSpawnPoint(planet, "Rebel Entrance", , , )
    return 
    
def kesselJTLSpawnPoints(core, planet):
    trvSvc = core.travelService
   
     trvSvc.addJTLSpawnPoint(planet, "Imperial Entrance", , , )
     trvSvc.addJTLSpawnPoint(planet, "Rebel Entrance", , , )
    return 
    
    
import sys

def setup(core, actor, buff):
	core.skillModService.addSkillMod(actor, 'dot_bleed', 30)
	return
	
def removeBuff(core, actor, buff):
	core.skillModService.deductSkillMod(actor, 'dot_bleed', 30)
	return
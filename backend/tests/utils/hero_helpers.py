from website.models import (
    Hero, PrimaryFire, SecondaryFire, AbilityE, AbilityShift, Ultimate, Passive
)
from website import db

def clone_hero_for_patch(hero, new_patch, overrides=None):
    overrides = overrides or {}

    cloned_hero = Hero(
        name = hero.name,
        health = overrides.get('health', hero.health),
        role = overrides.get('role', hero.role),
        patch = new_patch
    )
    db.session.add(cloned_hero)
    db.session.flush()

    if hero.primary_fire:
        db.session.add(PrimaryFire(
            hero_id = cloned_hero.id,
            patch_id = new_patch.id,
            name = overrides.get('primary_name', hero.primary_fire.name),
            damage = overrides.get('primary_damage', hero.primary_fire.damage),
            fire_rate = overrides.get('primary_fire_rate', hero.primary_fire.fire_rate),
            is_projectile = overrides.get('primary_is_projectile', hero.primary_fire.is_projectile)
        ))

    if hero.secondary_fire:
        db.session.add(SecondaryFire(
            hero_id = cloned_hero.id,
            patch_id = new_patch.id,
            name = overrides.get('secondary_name', hero.secondary_fire.name),
            damage = overrides.get('secondary_damage', hero.secondary_fire.damage),
            cooldown = overrides.get('secondary_cooldown', hero.secondary_fire.cooldown),
            is_projectile = overrides.get('secondary_is_projectile', hero.secondary_fire.is_projectile)
        ))

    if hero.ability_e:
        db.session.add(AbilityE(
            hero_id = cloned_hero.id,
            patch_id = new_patch.id,
            name = overrides.get('ability_e_name', hero.ability_e.name),
            cooldown = overrides.get('ability_e_cooldown', hero.ability_e.cooldown),
            description = overrides.get('ability_e_description', hero.ability_e.description)
        ))

    if hero.ability_shift:
        db.session.add(AbilityShift(
            hero_id = cloned_hero.id,
            patch_id = new_patch.id,
            name = overrides.get('ability_shift_name', hero.ability_shift.name),
            cooldown = overrides.get('ability_shift_cooldown', hero.ability_shift.cooldown),
            damage = overrides.get('ability_shift_damage', hero.ability_shift.damage),
            description = overrides.get('ability_shift_description', hero.ability_shift.description)
        ))

    if hero.ultimate:
        db.session.add(Ultimate(
            hero_id = cloned_hero.id,
            patch_id = new_patch.id,
            name = overrides.get('ultimate_name', hero.ultimate.name),
            charge_cost = overrides.get('ultimate_charge_cost', hero.ultimate.charge_cost),
            description = overrides.get('ultimate_description', hero.ultimate.description)
        ))

    if hero.passive:
        db.session.add(Passive(
            hero_id = cloned_hero.id,
            patch_id = new_patch.id,
            name = overrides.get('passive_name', hero.passive.name),
            cooldown = overrides.get('passive_cooldown', hero.passive.cooldown),
            trigger = overrides.get('passive_trigger', hero.passive.trigger),
            description = overrides.get('passive_description', hero.passive.description)
        ))

    return cloned_hero


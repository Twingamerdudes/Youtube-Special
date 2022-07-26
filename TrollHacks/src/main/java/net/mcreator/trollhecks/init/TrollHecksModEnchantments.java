
/*
 *    MCreator note: This file will be REGENERATED on each build.
 */
package net.mcreator.trollhecks.init;

import net.minecraftforge.registries.RegistryObject;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.DeferredRegister;

import net.minecraft.world.item.enchantment.Enchantment;

import net.mcreator.trollhecks.enchantment.IgnitementEnchantment;
import net.mcreator.trollhecks.enchantment.ExplosionEnchantment;
import net.mcreator.trollhecks.TrollHecksMod;

public class TrollHecksModEnchantments {
	public static final DeferredRegister<Enchantment> REGISTRY = DeferredRegister.create(ForgeRegistries.ENCHANTMENTS, TrollHecksMod.MODID);
	public static final RegistryObject<Enchantment> IGNITEMENT = REGISTRY.register("ignitement", () -> new IgnitementEnchantment());
	public static final RegistryObject<Enchantment> EXPLOSION = REGISTRY.register("explosion", () -> new ExplosionEnchantment());
}

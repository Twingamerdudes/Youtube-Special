
/*
 *    MCreator note: This file will be REGENERATED on each build.
 */
package net.mcreator.trollhecks.init;

import net.minecraftforge.registries.RegistryObject;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.common.ForgeSpawnEggItem;

import net.minecraft.world.item.Item;
import net.minecraft.world.item.CreativeModeTab;

import net.mcreator.trollhecks.item.HeartSwordItem;
import net.mcreator.trollhecks.item.HeartItem;
import net.mcreator.trollhecks.item.AmogusMeatItem;
import net.mcreator.trollhecks.TrollHecksMod;

public class TrollHecksModItems {
	public static final DeferredRegister<Item> REGISTRY = DeferredRegister.create(ForgeRegistries.ITEMS, TrollHecksMod.MODID);
	public static final RegistryObject<Item> HEART_SWORD = REGISTRY.register("heart_sword", () -> new HeartSwordItem());
	public static final RegistryObject<Item> HEART = REGISTRY.register("heart", () -> new HeartItem());
	public static final RegistryObject<Item> TROLL = REGISTRY.register("troll_spawn_egg",
			() -> new ForgeSpawnEggItem(TrollHecksModEntities.TROLL, -1, -16777216, new Item.Properties().tab(CreativeModeTab.TAB_MISC)));
	public static final RegistryObject<Item> AMOGUS_MEAT = REGISTRY.register("amogus_meat", () -> new AmogusMeatItem());
	public static final RegistryObject<Item> AMOGUS = REGISTRY.register("amogus_spawn_egg",
			() -> new ForgeSpawnEggItem(TrollHecksModEntities.AMOGUS, -65536, -16724737, new Item.Properties().tab(CreativeModeTab.TAB_MISC)));
}


package net.mcreator.trollhecks.enchantment;

import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.item.enchantment.EnchantmentCategory;
import net.minecraft.world.item.enchantment.Enchantment;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.entity.EquipmentSlot;

public class ExplosionEnchantment extends Enchantment {
	public ExplosionEnchantment(EquipmentSlot... slots) {
		super(Enchantment.Rarity.VERY_RARE, EnchantmentCategory.BREAKABLE, slots);
	}

	@Override
	public boolean canApplyAtEnchantingTable(ItemStack stack) {
		if (stack.getItem() == Blocks.TNT.asItem())
			return true;
		return false;
	}

	@Override
	public boolean isTreasureOnly() {
		return true;
	}

	@Override
	public boolean isCurse() {
		return true;
	}
}

package net.mcreator.trollhecks.procedures;

import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.effect.MobEffects;
import net.minecraft.world.effect.MobEffectInstance;

import net.mcreator.trollhecks.network.TrollHecksModVariables;

public class HeartProcedureProcedure {
	public static void execute(Entity entity) {
		if (entity == null)
			return;
		{
			double _setval = (entity.getCapability(TrollHecksModVariables.PLAYER_VARIABLES_CAPABILITY, null)
					.orElse(new TrollHecksModVariables.PlayerVariables())).PlayerHealthBoost + 1;
			entity.getCapability(TrollHecksModVariables.PLAYER_VARIABLES_CAPABILITY, null).ifPresent(capability -> {
				capability.PlayerHealthBoost = _setval;
				capability.syncPlayerVariables(entity);
			});
		}
		if (entity instanceof LivingEntity _entity)
			_entity.addEffect(new MobEffectInstance(MobEffects.HEALTH_BOOST, 900000000,
					(int) (entity.getCapability(TrollHecksModVariables.PLAYER_VARIABLES_CAPABILITY, null)
							.orElse(new TrollHecksModVariables.PlayerVariables())).PlayerHealthBoost,
					(false), (false)));
	}
}

package net.mcreator.trollhecks.procedures;

import net.minecraft.world.entity.player.Player;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.effect.MobEffects;
import net.minecraft.world.effect.MobEffectInstance;

import net.mcreator.trollhecks.network.TrollHecksModVariables;

public class HeartSwordProcedureProcedure {
	public static void execute(Entity entity, Entity sourceentity) {
		if (entity == null || sourceentity == null)
			return;
		double Health = 0;
		Entity Player = null;
		Health = entity instanceof LivingEntity _livEnt ? _livEnt.getHealth() : -1;
		Player = sourceentity;
		{
			double _setval = (sourceentity.getCapability(TrollHecksModVariables.PLAYER_VARIABLES_CAPABILITY, null)
					.orElse(new TrollHecksModVariables.PlayerVariables())).PlayerHealthBoost + 1;
			sourceentity.getCapability(TrollHecksModVariables.PLAYER_VARIABLES_CAPABILITY, null).ifPresent(capability -> {
				capability.PlayerHealthBoost = _setval;
				capability.syncPlayerVariables(sourceentity);
			});
		}
		if (entity instanceof LivingEntity _entity)
			_entity.addEffect(new MobEffectInstance(MobEffects.HEALTH_BOOST, 900000000, (int) (Health - 1), (false), (false)));
		if (Player instanceof LivingEntity _entity)
			_entity.addEffect(new MobEffectInstance(MobEffects.HEALTH_BOOST, 900000000,
					(int) (sourceentity.getCapability(TrollHecksModVariables.PLAYER_VARIABLES_CAPABILITY, null)
							.orElse(new TrollHecksModVariables.PlayerVariables())).PlayerHealthBoost,
					(false), (false)));
	}
}

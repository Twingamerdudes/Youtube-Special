package net.mcreator.trollhecks.procedures;

import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.eventbus.api.Event;
import net.minecraftforge.event.entity.player.PlayerEvent;

import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.effect.MobEffects;
import net.minecraft.world.effect.MobEffectInstance;

import net.mcreator.trollhecks.network.TrollHecksModVariables;

import javax.annotation.Nullable;

@Mod.EventBusSubscriber
public class OnSpawnProcedure {
	@SubscribeEvent
	public static void onPlayerRespawned(PlayerEvent.PlayerRespawnEvent event) {
		execute(event, event.getPlayer());
	}

	public static void execute(Entity entity) {
		execute(null, entity);
	}

	private static void execute(@Nullable Event event, Entity entity) {
		if (entity == null)
			return;
		if (entity instanceof LivingEntity _entity)
			_entity.addEffect(new MobEffectInstance(MobEffects.HEALTH_BOOST, 900000000,
					(int) (entity.getCapability(TrollHecksModVariables.PLAYER_VARIABLES_CAPABILITY, null)
							.orElse(new TrollHecksModVariables.PlayerVariables())).PlayerHealthBoost,
					(false), (false)));
	}
}

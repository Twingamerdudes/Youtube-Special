
/*
 *    MCreator note: This file will be REGENERATED on each build.
 */
package net.mcreator.trollhecks.init;

import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.client.event.EntityRenderersEvent;
import net.minecraftforge.api.distmarker.Dist;

import net.mcreator.trollhecks.client.renderer.TrollRenderer;
import net.mcreator.trollhecks.client.renderer.AmogusRenderer;

@Mod.EventBusSubscriber(bus = Mod.EventBusSubscriber.Bus.MOD, value = Dist.CLIENT)
public class TrollHecksModEntityRenderers {
	@SubscribeEvent
	public static void registerEntityRenderers(EntityRenderersEvent.RegisterRenderers event) {
		event.registerEntityRenderer(TrollHecksModEntities.TROLL.get(), TrollRenderer::new);
		event.registerEntityRenderer(TrollHecksModEntities.AMOGUS.get(), AmogusRenderer::new);
	}
}

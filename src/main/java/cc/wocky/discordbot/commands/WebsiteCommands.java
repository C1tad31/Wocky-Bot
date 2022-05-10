package cc.wocky.discordbot.commands;

import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.entities.Member;
import net.dv8tion.jda.api.events.interaction.command.SlashCommandInteractionEvent;
import net.dv8tion.jda.api.events.interaction.component.ButtonInteractionEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import net.dv8tion.jda.api.interactions.components.buttons.Button;

import java.awt.Color;
import java.time.Instant;

import org.jetbrains.annotations.NotNull;

public class WebsiteCommands extends ListenerAdapter {
    @Override
    public void onSlashCommandInteraction(@NotNull SlashCommandInteractionEvent event) {
        Member member = event.getMember();
        if (event.getName().equals("website")) {
            EmbedBuilder embedBuilder = new EmbedBuilder()
                .setAuthor(member.getUser().getAsTag(), member.getUser().getAvatarUrl(), member.getUser().getAvatarUrl())
                .setTitle("Website Links")
                .setDescription("Here are a few of our links below")
                .setThumbnail(event.getGuild().getIconUrl())
                .setColor(Color.BLACK)
                .setTimestamp(Instant.now())
                .setFooter("Wocky Bot | Made by: Citadel", member.getUser().getAvatarUrl());
            event.replyEmbeds(embedBuilder.build()).addActionRow(
                Button.link("https://dc.wocky.cc/", "Wocky III Server"),
                Button.link("https://wfx.wocky.cc/", "WockyFX Server"),
                Button.link("https://discord.gg/FaMZU2h8fr", "Wocky API Server"),
                Button.link("https://discord.gg/EsP5DdvK", "Wocky Bot Server"),
                Button.link("https://t.me/WockyServices", "Wocky Services Telegram")).queue();
        }
    }

    @Override
    public void onButtonInteraction(@NotNull ButtonInteractionEvent event) {
        if (event.getComponentId().equals("website")) {
            event.reply("Thank you for your interest in Wocky Services for more information please contact on of the following people:\n<@961071033123741727> - ``Owner / Founder / Project Director / Developer``\n<@960758452232286208> - ``Co-Founder / Project Director / Developer``\n<@950157500706074625> - ``Leader / Project Director/ Developer``").queue();
        }
    }
}

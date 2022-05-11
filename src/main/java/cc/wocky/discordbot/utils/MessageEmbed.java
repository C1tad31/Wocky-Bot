package cc.wocky.discordbot.utils;

import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.entities.Member;
import net.dv8tion.jda.api.events.guild.GuildJoinEvent;
import net.dv8tion.jda.api.events.guild.member.GuildMemberJoinEvent;
import net.dv8tion.jda.api.events.interaction.ModalInteractionEvent;
import net.dv8tion.jda.api.events.interaction.command.SlashCommandInteractionEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

import java.awt.*;
import java.time.Instant;

public class MessageEmbed extends ListenerAdapter {

    public static void createEmbed(SlashCommandInteractionEvent event, String choice, Member author, String title, String url, String imageUrl, String desc, String thumbnail, String color, Instant timestamp, String footer) {
        switch (choice) {
            case "eph":
                EmbedBuilder successEmbed = new EmbedBuilder()
                        .setAuthor(author.getUser().getAsTag(), author.getUser().getAvatarUrl(), author.getUser().getAvatarUrl())
                        .setTitle(title, url)
                        .setDescription(desc)
                        .setColor(Color.decode(color))
                        .setImage(imageUrl)
                        .setThumbnail(thumbnail)
                        .setTimestamp(timestamp)
                        .setFooter(footer);
                event.replyEmbeds(successEmbed.build()).setEphemeral(true).queue();
            case "reg":
                EmbedBuilder errorEmbed = new EmbedBuilder()
                        .setAuthor(author.getUser().getAsTag(), author.getUser().getAvatarUrl(), author.getUser().getAvatarUrl())
                        .setTitle(title, url)
                        .setDescription(desc)
                        .setColor(Color.decode(color))
                        .setImage(imageUrl)
                        .setThumbnail(thumbnail)
                        .setTimestamp(timestamp)
                        .setFooter(footer);
                event.replyEmbeds(errorEmbed.build()).queue();
        }
    }
}

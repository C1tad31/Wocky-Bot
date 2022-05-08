package cc.wocky.discordbot.events;

import java.time.Instant;

import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.entities.Member;
import net.dv8tion.jda.api.entities.TextChannel;
import net.dv8tion.jda.api.events.guild.member.GuildMemberRemoveEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

public class MemberRemove extends ListenerAdapter {
    public void onMemberRemove(GuildMemberRemoveEvent event) {
        try {
            Member member = event.getMember();
            TextChannel channel = event.getGuild().getTextChannelsByName("welcome", true).get(0);
            EmbedBuilder embedBuilder = new EmbedBuilder()
                .setAuthor(member.getUser().getAsTag())
                .setTitle("Member Left!")
                .setDescription(String.format("%s has left the server!", member.getUser().getAsMention()))
                .setTimestamp(Instant.now())
                .setThumbnail(event.getGuild().getIconUrl())
                .setFooter("Wocky Bot | Made by: Citadel");
                channel.sendMessageEmbeds(embedBuilder.build()).queue();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

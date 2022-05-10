package cc.wocky.discordbot.events;

import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.entities.Member;
import net.dv8tion.jda.api.entities.PrivateChannel;
import net.dv8tion.jda.api.entities.TextChannel;
import net.dv8tion.jda.api.entities.User;
import net.dv8tion.jda.api.events.guild.member.GuildMemberJoinEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import org.jetbrains.annotations.NotNull;

import java.time.Instant;

public class MemberJoin extends ListenerAdapter {
    @Override
    public void onGuildMemberJoin(@NotNull GuildMemberJoinEvent event) {
        User user = event.getUser();
        PrivateChannel privateChannel = user.openPrivateChannel().complete();
        privateChannel.sendMessage("Welcome to " + event.getGuild().getName() + ", please make sure to look at <#973416853718331412> and follow the rules!").queue();
        Member member = event.getMember();
        TextChannel channel = event.getGuild().getTextChannelsByName("welcome", true).get(0);
        EmbedBuilder embedBuilder = new EmbedBuilder()
                .setAuthor(member.getUser().getAsTag())
                .setTitle("New Member!")
                .setDescription(String.format("%s has joined the server!", member.getUser().getAsMention()))
                .setTimestamp(Instant.now())
                .setThumbnail(event.getGuild().getIconUrl())
                .setFooter("Wocky Bot | Made by: Citadel");
        channel.sendMessageEmbeds(embedBuilder.build()).queue();
    }
}

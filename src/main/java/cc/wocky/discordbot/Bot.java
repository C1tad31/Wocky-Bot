package cc.wocky.discordbot;

import cc.wocky.discordbot.commands.HelpCommand;
import cc.wocky.discordbot.commands.SupportCommand;
import cc.wocky.discordbot.commands.WebsiteCommands;
import cc.wocky.discordbot.events.BotReady;
import cc.wocky.discordbot.events.MemberJoin;
import cc.wocky.discordbot.events.MemberRemove;
import cc.wocky.discordbot.modcommands.*;
import cc.wocky.discordbot.reputation.ReputationCommand;
import net.dv8tion.jda.api.JDA;
import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.OnlineStatus;
import net.dv8tion.jda.api.entities.Activity;
import net.dv8tion.jda.api.interactions.commands.OptionType;
import net.dv8tion.jda.api.interactions.commands.build.OptionData;

import javax.security.auth.login.LoginException;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class Bot {
    private static JDA jda;
    private static final Thread alternateGameThread = new Thread("AlternateGameThread") {
        @Override
        public void run() {
            while (true) {
                jda.getPresence().setPresence(OnlineStatus.DO_NOT_DISTURB, Activity.watching(String.format("Over %s Guilds", jda.getGuilds().size())));
                try {Thread.sleep(5000);} catch (InterruptedException e) {e.printStackTrace();}
                jda.getPresence().setPresence(OnlineStatus.DO_NOT_DISTURB, Activity.watching("dc.wocky.cc"));
                try {Thread.sleep(5000);} catch (InterruptedException e) {e.printStackTrace();}
            }
        }
    };
    private static String token;
    public static void main(String[] args) throws IOException, LoginException {
        File file = new File("/home/citadel/Desktop/Wocky-Bot/src/main/java/cc/wocky/discordbot/config/config.txt");
        BufferedReader reader = new BufferedReader(new FileReader(file));
        while((token = reader.readLine()) != null) {
            jda = JDABuilder.createDefault(Bot.token).build();
            jda.addEventListener(new BotReady());
            // Bot Events
            jda.addEventListener(new MemberJoin());
            jda.addEventListener(new MemberRemove());
            // Bot Commands
            jda.addEventListener(new HelpCommand());
            jda.upsertCommand("help", "Displays the Bot Help Menu").queue();

            jda.addEventListener(new SupportCommand());
            jda.upsertCommand("support", "Create a support ticket").queue();

            jda.addEventListener(new ClearCommand());
            jda.upsertCommand("clear", "Clear a specific amount of messages from the chat").addOptions(
                new OptionData(OptionType.INTEGER, "amount", "Clear the specified amount of messages from the chat", true), 
                new OptionData(OptionType.CHANNEL, "channel", "channel to clear message from", true)).queue();

            jda.addEventListener(new KickCommand());
            jda.upsertCommand("kick", "Kick a Specified user from the chat").addOptions(
                new OptionData(OptionType.MENTIONABLE, "member", "User to be kicked", true),
                new OptionData(OptionType.STRING, "reason", "reason for kick", true)).queue();

            jda.addEventListener(new BanCommand());
            jda.upsertCommand("ban", "Ban a Specified user from the chat").addOptions(
                new OptionData(OptionType.MENTIONABLE, "member", "User to be banned", true),
                new OptionData(OptionType.STRING, "reason", "reason for Ban", true)).queue();

            jda.addEventListener(new WebsiteCommands());

            jda.addEventListener(new LockdownCommand());
            jda.upsertCommand("lockdown", "Lockdown a specified chat").addOptions(
                new OptionData(OptionType.CHANNEL, "channel", "Channel to be locked", true)).queue();

            jda.addEventListener(new UnlockCommand());
            jda.upsertCommand("unlock", "Unlock a specified chat").addOptions(
                    new OptionData(OptionType.CHANNEL, "channel", "Channel to be unlocked", true)).queue();

            jda.addEventListener(new MuteCommand());
            jda.upsertCommand("mute", "Mute a specific user in chat").addOptions(
                new OptionData(OptionType.MENTIONABLE, "member", "User to be muted", true)).queue();

            jda.addEventListener(new UnmuteCommand());
            jda.addEventListener(new UnmuteCommand());
            jda.upsertCommand("unmute", "Unmute a specific user in chat").addOptions(
                    new OptionData(OptionType.MENTIONABLE, "member", "User to be unmuted", true)).queue();

            jda.addEventListener(new ReputationCommand());
            jda.upsertCommand("rep", "Give a Specified User Reputation points").addOptions(
                    new OptionData(OptionType.MENTIONABLE, "member", "User to be repped", true),
                    new OptionData(OptionType.INTEGER, "num", "Number of rep points you would like to give", true)).queue();

            jda.addEventListener(new WebsiteCommands());
            jda.upsertCommand("website", "Links to our websites").queue();

            jda.addEventListener(new ChannelDeleteInterval());
            jda.upsertCommand("autodelete", "Deletes the channel on an interval of 12 hours").addOptions(
            new OptionData(OptionType.CHANNEL, "channel", "channel to set AutoDelete on", true)).queue();

            jda.addEventListener(new NukeCommand());
            jda.upsertCommand("nuke", "Nukes a channel").queue();


            alternateGameThread.start();
        }
    }
}

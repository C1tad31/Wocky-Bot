package cc.wocky.discordbot;

import cc.wocky.discordbot.commands.HelpCommand;
import cc.wocky.discordbot.commands.SupportCommand;
import cc.wocky.discordbot.commands.WebsiteCommands;
import cc.wocky.discordbot.events.BotReady;
import cc.wocky.discordbot.events.MemberJoin;
import cc.wocky.discordbot.events.MemberRemove;
import cc.wocky.discordbot.modcommands.ClearCommand;
import cc.wocky.discordbot.modcommands.KickCommand;
import lombok.Getter;
import lombok.Setter;
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

@Getter
@Setter
public class Bot {
    private static JDA jda;
    private static Thread alternateGameThread = new Thread("AlternateGameThread") {
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
    public static void main(String[] args) throws IOException, LoginException, InterruptedException {
        File file = new File("/home/citadel/Desktop/WockyBot/src/main/java/cc/wocky/discordbot/config/config.txt");
        BufferedReader reader = new BufferedReader(new FileReader(file));
        while((token = reader.readLine()) != null) {
            jda = JDABuilder.createDefault(Bot.token).build().awaitReady();
            // Bot Events
            jda.addEventListener(new BotReady());
            jda.addEventListener(new MemberJoin());
            jda.addEventListener(new MemberRemove());
            // Bot Commands
            jda.addEventListener(new HelpCommand());
            jda.upsertCommand("help", "Displays the Bot Help Menu").queue();
            jda.addEventListener(new SupportCommand());
            jda.upsertCommand("support", "Create a support ticket").queue();
            jda.addEventListener(new ClearCommand());
            jda.upsertCommand("clear", "Clear a specific amount of messages from the chat").addOptions(new OptionData(OptionType.INTEGER, "amount", "Clear the specified amount of messages from the chat", true), 
            new OptionData(OptionType.CHANNEL, "channel", "channel to clear message from", true)).queue();
            jda.addEventListener(new KickCommand());
            jda.upsertCommand("kick", "Kick a Specified user from the chat").addOptions(new OptionData(OptionType.MENTIONABLE, "member", "User to be kicked", true),
            new OptionData(OptionType.STRING, "reason", "reason for kick", true)).queue();
            jda.upsertCommand("ban", "Ban a Specified user from the chat").addOptions(new OptionData(OptionType.MENTIONABLE, "member", "User to be banned", true),
            new OptionData(OptionType.STRING, "reason", "reason for Ban", true)).queue();
            jda.addEventListener(new WebsiteCommands());
            jda.upsertCommand("website", "Links to our websites").queue();


            alternateGameThread.start();
        }
    }
}

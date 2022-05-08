package cc.wocky.discordbot.commands;

import net.dv8tion.jda.api.entities.Member;
import net.dv8tion.jda.api.events.interaction.ModalInteractionEvent;
import net.dv8tion.jda.api.events.interaction.command.SlashCommandInteractionEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import net.dv8tion.jda.api.interactions.components.ActionRow;
import net.dv8tion.jda.api.interactions.components.Modal;
import net.dv8tion.jda.api.interactions.components.text.TextInput;
import net.dv8tion.jda.api.interactions.components.text.TextInputStyle;
import org.jetbrains.annotations.NotNull;

import javax.annotation.Nonnull;

public class SupportCommand extends ListenerAdapter {
    @Override
    public void onSlashCommandInteraction(@NotNull SlashCommandInteractionEvent event) {
        if (event.getName().equals("support")) {
            TextInput title = TextInput.create("title", "Title", TextInputStyle.SHORT)
                    .setPlaceholder("Title you Support Ticket")
                    .setMinLength(1)
                    .setMaxLength(100)
                    .build();
            TextInput email = TextInput.create("email", "Email", TextInputStyle.SHORT)
                    .setPlaceholder("Email for us to reach you at later")
                    .setMinLength(1)
                    .setMaxLength(100)
                    .build();
            TextInput message = TextInput.create("message", "Message", TextInputStyle.PARAGRAPH)
                    .setPlaceholder("Enter your Message...")
                    .setMinLength(1)
                    .setMaxLength(100)
                    .build();

            Modal modal = Modal.create("support", "Create a Support Ticket")
                    .addActionRows(ActionRow.of(title), ActionRow.of(email), ActionRow.of(message))
                    .build();

            event.replyModal(modal).queue();
        }
    }

    public void onModalInteraction(@Nonnull ModalInteractionEvent event) {
        if (event.getModalId().equals("support")) {
            String title = event.getValue("title").getAsString();
            String email = event.getValue("email").getAsString();
            String message = event.getValue("message").getAsString();

            createSupportTicket(event, title, email, message);

        }
    }

    public void createSupportTicket(ModalInteractionEvent event, String title, String email, String message) {
        Member member = event.getMember();
        event.getGuild().createTextChannel("ticket-" + event.getUser().getName()).addPermissionOverride(member, null, null).queue(textChannel -> {
//            textChannel.sendMessage(String.format("%s\n\n\nSupport is on is way!\n\n**Title**: %s\n**Email**: %s\n**Message**: %s", event.getUser().getAsMention(), title, email, message)).queue();
//            MessageEmbed.createOtherEmbed(event, "reg", member, "Support Ticket for: " + textChannel.getName(), "https://wocky.cc/", null, String.format("Support is on is way!\n\n**Title**: %s\n**Email**: %s\n**Message**: %s", title, email, message), textChannel.getGuild().getIconUrl(), "#000000", Instant.now(), "Wocky Bot | Made by: Citadel");
        });
    }
}

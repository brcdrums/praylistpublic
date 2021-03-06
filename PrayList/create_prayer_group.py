{% extends "base.html" %}
{% block content %}
    <h1 class = >Submit a Prayer</h1>

    {% if form.errors %}
        <p style="color: red;">
            Please correct the error{{ form.errors|pluralize }} below.
        </p>
    {% endif %}

    <form action="" method="post"> {% csrf_token %}
        <div class="field">
            {{ form.subject.errors }}
            <label for="subject">Subject:</label>
            {{ form.subject }}
        </div>
        <div class="spacer"></div>
        <div class="field">
            {{ form.prayer.errors }}
            <label for="prayer">Prayer:</label>
            {{ form.prayer }}
        </div>
        <div class="spacer"></div>
        <input type="submit" valdue="Submit">
    </form>
</body>
</html>
{% endblock %}
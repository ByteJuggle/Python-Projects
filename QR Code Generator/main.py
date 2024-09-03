import qrcode as qr
img= qr.make("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.reddit.com%2Fr%2FDemonSlayerAnime%2Fcomments%2Fpnn9j9%2Flets_be_honest_the_only_person_that_giyuu_treats%2F&psig=AOvVaw03t6mJ5W-3TcgOy9E2K6hF&ust=1725462379672000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOD74bWGp4gDFQAAAAAdAAAAABAJ")
img.save("Result.png")